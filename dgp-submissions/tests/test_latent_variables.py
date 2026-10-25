"""Latent-variable indexing must use existing structured ZIP fields, not execute code."""
import unittest
from pathlib import Path
from tools.dgp_registry.latent_variables import latent_from_collection
from tools.dgp_registry.zip_reader import read_archive


class LatentCollectionTests(unittest.TestCase):
    def test_existing_proximal_structured_zip(self):
        records, warnings = read_archive(Path('examples/proximal_10_dgps.zip'))
        index = {r['record_id']:r for r in records}
        self.assertEqual(len(index), 10)
        expected = {
            'proximal-cui-2024-linear-v1':{'U'},
            'proximal-dukes-2023-mediation-v1':{'U'},
            'proximal-imbens-2025-longterm-v1':{'X̃','U'},
            'proximal-shi-2026-sc-gaussian-v1':{'λ_tk'},
            'proximal-shi-2026-sc-poisson-v1':{'λ_t'},
            'proximal-su-2026-transport-v1':{'V','Uj'},
            'proximal-ying-2023-longitudinal-v1':{'U0','U1'}
        }
        for rid,wanted in expected.items():
            record=index[rid]
            names={row['name'] for row in record['mechanism']['latent_variables']}
            self.assertTrue(names>=wanted,(rid,names,wanted))
            self.assertEqual(record['mechanism']['latent_variables_status'],
                             'candidates_from_equations_need_review')
            self.assertFalse(names & {'A','Z','W','X1','X2','Y'},(rid,names))

    def test_explicit_metadata_is_preserved(self):
        rows,status=latent_from_collection(
            {'equations':['U~N(0,1)'],
             'latent_variables':[{'name':'U','role':'unmeasured_confounder','dimension':1}]},[])
        self.assertEqual(status,'explicit_structured_metadata')
        self.assertEqual(rows[0]['role'],'unmeasured_confounder')
        self.assertEqual(rows[0]['dimension'],1)

    def test_empty_explicit_list_is_distinct_from_unknown(self):
        self.assertEqual(latent_from_collection({'equations':['X=1'],'latent_variables':[]},[])[1],
                         'explicit_structured_metadata')
        self.assertEqual(latent_from_collection({'equations':['X=1']},[])[1],
                         'not_explicitly_specified')

    def test_noise_not_confused_with_latent(self):
        result,status=latent_from_collection(
            {'equations':['X~N(0,1); epsilon~N(0,1); A|X~Bernoulli(.5)']},
            [{'name':'X'},{'name':'A'}])
        self.assertEqual(result,[])
        self.assertEqual(status,'not_explicitly_specified')

    def test_indexed_observed_variables_are_not_latent(self):
        rows,_=latent_from_collection(
            {'equations':['Zⱼ iid N(0,1), j=1,...,10',
                          '(ξ,ε) joint normal: mean 0, variances 1, correlation 0.8']},
            [{'name':'Z'+str(j)} for j in range(1,11)])
        self.assertEqual([x['name'] for x in rows],['ξ'])

    def test_grouped_latent_noise_declaration(self):
        rows,_=latent_from_collection(
            {'equations':['Z~Normal(0,2), U~Normal(0,2), delta,zeta~Normal(0,0.1)']},
            [{'name':'Z'}])
        self.assertEqual([x['name'] for x in rows],['U','delta','zeta'])

    def test_explicitly_labeled_latent_intermediate(self):
        rows,_=latent_from_collection(
            {'equations':[{'label':'Latent fixed effect',
                           'expression':'v=D*f(Z)+eta; eta~N(0,1)'}]},
            [{'name':'D'},{'name':'Z1'}])
        self.assertIn('v',[r['name'] for r in rows])

    def test_conditional_source_sampling_not_latent(self):
        rows,_=latent_from_collection(
            {'equations':['A|S=1~Bernoulli(0.5); Z|X,U,S=1~N(0,1)']},
            [{'name':'S'},{'name':'SA'},{'name':'SZ1'},{'name':'X1'}])
        self.assertEqual(rows,[])


if __name__=='__main__':
    unittest.main()
