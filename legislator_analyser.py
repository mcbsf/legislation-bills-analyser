from copy import deepcopy
class LegislatorAnalyser:
    #clean code misuse, generic name 'Analyser' usually implies more than 1 purpose. possible refactor
    def __init__(self, legislators_df, vote_results_df) -> None:
        self.legislators_df = deepcopy(legislators_df) 
        self.vote_results_df = deepcopy(vote_results_df) 
    
    
    def split_votes_count_by_vote_type(self):
        self.vote_results_df['count'] = 1
        self.vote_results_df = self.vote_results_df.pivot_table(index='legislator_id', columns='vote_type', values='count', aggfunc='sum')
        self.vote_results_df.columns = ['num_supported_bills', 'num_opposed_bills']
        self.vote_results_df = self.vote_results_df.reset_index()

    def get_legislators_name(self):
        self.vote_results_df = self.vote_results_df.merge(self.legislators_df, on='legislator_id', how='left')

    def parse_legislators_id_column_to_match_vote_results(self):
        self.legislators_df = self.legislators_df.rename(columns={'id': 'legislator_id'})
    
    def get_vote_results_legislators_names(self):
        self.vote_results_df['legislators_name']

    def write_csv_by_vote_type(self):
        self.vote_results_df[['name', 'num_supported_bills', 'num_opposed_bills']].to_csv('output/legislators-support-oppose-count.csv', index = False)