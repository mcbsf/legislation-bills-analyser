import pandas as pd
from analysers.legislator_analyser import LegislatorAnalyser
from analysers.bills_analyser import BillsAnalyser

bills_df = pd.read_csv('input/bills.csv')
legislators_df = pd.read_csv('input/legislators.csv')
votes_df = pd.read_csv('input/votes.csv')
vote_results_df = pd.read_csv('input/vote_results.csv')

legislator_analyser = LegislatorAnalyser(legislators_df, vote_results_df)
legislator_analyser.parse_legislators_id_column_to_match_vote_results()
legislator_analyser.split_votes_count_by_vote_type()
legislator_analyser.get_legislators_name()
legislator_analyser.write_csv()

bills_analyser = BillsAnalyser(votes_df, bills_df, vote_results_df, legislators_df)
bills_analyser.parse_columns_to_match_pandas_merge()
bills_analyser.get_votes_by_bill()
bills_analyser.split_votes_count_by_vote_type()
bills_analyser.parse_column_names_to_expected_output()
bills_analyser.order_columns_to_expected_output()
bills_analyser.write_csv()