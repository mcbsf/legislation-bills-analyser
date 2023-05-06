from copy import deepcopy
class BillsAnalyser:
    #clean code warning, generic name 'Analyser' usually implies more than 1 purpose. possible refactor
    def __init__(self, votes_df, bills_df, vote_results_df, legislator_df) -> None:
        self.votes_df = deepcopy(votes_df)
        self.vote_results_df = deepcopy(vote_results_df) 
        self.bills_df = deepcopy(bills_df) 
        self.legislator_df = deepcopy(legislator_df) 
    
    def parse_columns_to_match_pandas_merge(self):
        self.votes_df = self.votes_df.rename(
            columns={'id': 'vote_id'}
        )
        self.bills_df = self.bills_df.rename(
            columns={
                'id': 'bill_id',
                'sponsor_id': 'legislator_id'
            }
        )

        self.bills_df = self.bills_df.rename(
            columns={'id': 'bill_id'}
        )

        self.legislator_df = self.legislator_df.rename(
            columns={'id': 'legislator_id'}
        )

    def get_votes_by_bill(self):
        self.votes_df = self.votes_df.merge(self.vote_results_df[['id','vote_id','vote_type']], on='vote_id', how='left')
        self.bills_df = self.bills_df.merge(self.votes_df, on='bill_id', how='left')
        self.bills_df = self.bills_df.merge(self.legislator_df, on='legislator_id', how='left').fillna('Unknown')

    def split_votes_count_by_vote_type(self):
        self.bills_df['count'] = 1
        self.bills_df = self.bills_df.pivot_table(index=['bill_id', 'title', 'name'], columns='vote_type', values='count', aggfunc='sum')
        self.bills_df.columns = ['supporter_count', 'opposer_count']
        self.bills_df = self.bills_df.reset_index()

    def write_csv(self):
        self.bills_df.to_csv('output/bills-support-oppose-count.csv', index = False)

    def get_sponsor_name(self):
        self.bills_df = self.bills_df.merge(self.legislator_df, on='legislator_id', how='left')

    def parse_column_names_to_expected_output(self):
        self.bills_df = self.bills_df.rename(
            columns = {
                'bill_id': 'id',
                'name': 'primary_sponsor'
            }
        )
    
    def order_columns_to_expected_output(self):
        self.bills_df = self.bills_df[['id', 'title',  'supporter_count', 'opposer_count', 'primary_sponsor']]