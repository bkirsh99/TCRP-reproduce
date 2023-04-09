from glob import glob
import os
import argparse

def make_chunks(iterable, nchunks): 
    length = len(iterable)
    chunk_size = (length // nchunks) 
    remainder = length % nchunks

    chunks = []
    i = 0
    while i < length:
        if remainder != 0: 
            end = i + chunk_size + 1
            remainder -= 1
        else: 
            end = i + chunk_size

        chunks.append(iterable[i:end])
        i = end

    return chunks


filepath = os.path.realpath(__file__)
dir_name = os.path.dirname(filepath)
home_dir = os.path.dirname(dir_name)

out_dir = home_dir + '/' + 'data/output/'
run_dir = out_dir + 'runs/'
work_dic = out_dir + 'cell_line_lists/'

n_gpus = 20

#run_mode = "tcrp" # "tcrp" or "baseline"
#run_name = "260305_tcrp_run"
#dataset = "GDSC"
#tissue = "central_nervous_system"
parser = argparse.ArgumentParser()

parser.add_argument('--dataset', type=str, default='GDSC', help='dataset to perform crossvalidation on')
parser.add_argument('--tissue', type=str, default='urinary_tract', help='Validation tissue, using the rest tissues for training')

args = parser.parse_args()
dataset = args.dataset
tissue = args.tissue

run_name = dataset + '_' + tissue
out_directory = run_dir + run_name
task_directory = out_directory + '/' + 'tasks'

os.system("mkdir -p {}".format(task_directory))

#drugs = glob(work_dic + "*.pkl")
#drugs = [drug.split('/')[-1].split('_tissue_cell_line_list.pkl')[0] for drug in drugs]

priority_drugs_file = dir_name + '/' + 'priority_drugs' 

with open(priority_drugs_file) as f: 
    priority = [i.strip() for i in f.readlines()]

print("Drugs to run: ")
print(priority)
print("Total number of drugs to run: {}".format(len(priority)))

#missing = set(priority).difference(drugs)
#print("Following drugs are missing: ")
#print(missing)
#print(len(missing))

#remaining_drugs = list(set(drugs).difference(priority))
#priority = list(set(priority).difference(missing))
#remaining_drugs_chunked = make_chunks(remaining_drugs, n_gpus)
priority_chunked = make_chunks(priority, n_gpus)

#print("Total number of drugs: {}".format(len(priority) + len(remaining_drugs)))

fewshot_data_path = home_dir + '/' + 'data/fewshot_data/' + dataset

for i, (b) in enumerate(zip(priority_chunked)):
#for i, (a, b) in enumerate(zip(priority_chunked, remaining_drugs_chunked)):
    #_drugs = a + b
    _drugs = b[0]
    drug_input_file = task_directory + '/drugs_input_{}'.format(i)
    with open(drug_input_file, 'w') as f: 
        f.write('\n'.join(_drugs))

    '''
    if run_mode == "tcrp": 
        cmd = ['python', home_dir + '/pipelines/' + 'generate_MAML_job_cv.py', '--run_name', run_name, '--drug_list_file', drug_input_file, '--job_id', str(i), '--job', 'drugs']
        cmd = ' '.join(cmd)
        print(cmd)
        os.system(cmd)

    elif run_mode == "baseline": 
        cmd = ['python', home_dir + '/pipelines/' + 'generate_baseline_job_cv.py', '--run_name', run_name, '--drug_list_file', drug_input_file, '--job_id', str(i), '--job', 'drugs', '--fewshot_data_path', fewshot_data_path]
        cmd = ' '.join(cmd)
        print(cmd)
        os.system(cmd)


    break
    '''
    tcrp_cmd = ['python', home_dir + '/pipelines/generate_MAML_job_cv.py', '--dataset',dataset,'--tissue',tissue,'--run_name', run_name, '--drug_list_file', drug_input_file, '--job_id', str(i), '--job', 'drugs']
    tcrp_cmd = ' '.join(tcrp_cmd)

    baseline_cmd = ['python', home_dir + '/pipelines/generate_baseline_job_cv.py','--dataset',dataset,'--tissue',tissue, '--run_name', run_name, '--drug_list_file', drug_input_file, '--job_id', str(i), '--job', 'drugs', '--fewshot_data_path', fewshot_data_path]
    baseline_cmd = ' '.join(baseline_cmd)
    

    print(tcrp_cmd)
    os.system(tcrp_cmd)

    print(baseline_cmd)
    os.system(baseline_cmd)
