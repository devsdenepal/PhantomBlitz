import subprocess
def generate_wlan_profile():
    result = subprocess.run(["netsh wlan show profile"], stdout=subprocess.PIPE)
    statement = result.stdout.decode('utf-8')
def generate_wlan_ind_profile(profile_name):
    result = subprocess.run([(f"netsh wlan show profile name= {profile_name} key=clear"],stdout=subprocess.PIPE)
    statement = result.stdout.decode('utf-8')                     