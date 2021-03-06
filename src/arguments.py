import argparse


def parse_args_train():
    parser = argparse.ArgumentParser(description='')
    arg = parser.add_argument
    arg('--pretrained_checkpoint', type=str, default='/gpfsnyu/scratch/yw3642/hf-models/microsoft_deberta-base')
    arg('--data_path', type=str, default='../data/train_processed.pkl')
    arg('--epochs', type=int, default=5)
    arg('--batch_size', type=int, default=16)
    arg('--accumulation_steps', type=int, default=1)
    arg('--lr', type=float, default=2e-5)
    arg('--weight_decay', type=float, default=0.01)
    arg('--seed', type=int, default=42)
    arg("--do_fix_offsets", default=False, action="store_true", help="fix offsets (force trim_offsets=False)")
    arg("--fold", default=-1, type=int)
    return parser.parse_args()

def parse_args_infer():
    parser = argparse.ArgumentParser(description='')
    arg = parser.add_argument
    arg('--pretrained_checkpoints', nargs='+', required=True)
    arg('--data_dir', type=str, default='../data/nbme-score-clinical-patient-notes/')
    arg('--batch_size', type=int, default=32)
    arg('--portion', type=float, default=1.0)
    arg("--pin_memory", default=False, action="store_true")
    arg("--cache", default=False, action="store_true")
    return parser.parse_args()


def parse_args_eval():
    parser = argparse.ArgumentParser(description='')
    arg = parser.add_argument
    arg('--data_path', type=str, default='../data/train_processed.pkl')
    arg('--pretrained_checkpoint', type=str, required=True)
    arg('--model_dir', type=str, required=True)
    arg("--do_fix_offsets", default=False, action="store_true", help="fix offsets (force trim_offsets=False)")
    return parser.parse_args()

def parse_args_pretrain():
    parser = argparse.ArgumentParser(description='')
    arg = parser.add_argument
    arg('--pretrained_checkpoint', type=str, default='/gpfsnyu/scratch/yw3642/hf-models/microsoft_deberta-base')
    arg('--data_path', type=str, default='../data/nbme-score-clinical-patient-notes/patient_notes.csv')
    arg('--epochs', type=int, default=1)
    arg('--batch_size', type=int, default=4)
    arg('--accumulation_steps', type=int, default=1)
    arg('--lr', type=float, default=1e-5)
    arg('--weight_decay', type=float, default=0.0)
    arg('--mlm_prob', type=float, default=0.2)
    arg('--seed', type=int, default=42)
    arg('--resume', type=str, default='')
    arg('--save_total_limit', type=int, default=2)
    return parser.parse_args()

def parse_args_blend():
    parser = argparse.ArgumentParser(description='')
    arg = parser.add_argument
    arg('--result_dirs', nargs='+', required=True)
    arg('--data_path', type=str, default='../data/train_processed.pkl')
    arg('--n_trials', type=int, default=100)
    arg('--out_dir', type=str, default='../data/')
    arg('--n_jobs', type=int, default=1)
    return parser.parse_args()


def parse_args_pl_infer():
    parser = argparse.ArgumentParser(description='')
    arg = parser.add_argument
    arg('--pretrained_checkpoint', type=str, required=True)
    arg('--model_dir', type=str, required=True)
    arg('--data_path', type=str, default='../data/train_pl_all.pkl')
    arg('--batch_size', type=int, default=16)
    arg("--do_fix_offsets", default=False, action="store_true", help="fix offsets (force trim_offsets=False)")
    return parser.parse_args()


def parse_args_pl_blend():
    parser = argparse.ArgumentParser(description='')
    arg = parser.add_argument
    arg('--blend_log', type=str, required=True)
    arg('--data_path', type=str, default='../data/train_pl_all.pkl')
    arg('--out_dir', type=str, default='../data/')
    return parser.parse_args()


def parse_args_train_pl():
    parser = argparse.ArgumentParser(description='')
    arg = parser.add_argument
    arg('--pretrained_checkpoint', type=str, default='/gpfsnyu/scratch/yw3642/hf-models/microsoft_deberta-base')
    arg('--data_path', type=str, default='../data/train_processed.pkl')
    arg('--pl_path', type=str, required=True)
    arg('--epochs', type=int, default=5)
    arg('--batch_size', type=int, default=16)
    arg('--accumulation_steps', type=int, default=1)
    arg('--lr', type=float, default=2e-5)
    arg('--weight_decay', type=float, default=0.01)
    arg('--seed', type=int, default=42)
    arg("--do_fix_offsets", default=False, action="store_true", help="fix offsets (force trim_offsets=False)")
    arg("--fold", default=-1, type=int)
    return parser.parse_args()