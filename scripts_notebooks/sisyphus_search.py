import pandas as pd
import subprocess

soft = pd.read_csv('data/2.0_unique_soft_wo_alt.csv')
soft_list = pd.Series(soft['0']).tolist()

soft_in_sisyphus_dict = {}

for name in soft_list:
  result = subprocess.run(['apt-cache', 'search', name], stdout=subprocess.PIPE)
  soft_in_sisyphus_dict[name] = result.stdout.decode('utf-8')


soft_in_sisyphus = pd.DataFrame([soft_in_sisyphus_dict])
soft_in_sisyphus.to_csv('data/2.1_alt_unique_soft.csv', index=False)
