# coding:utf-8

from pathlib import Path
MAIN_PATH = Path(__file__).absolute().parent.parent.parent

# data
DATA_PATH = MAIN_PATH / 'data/test_data.txt'
VOCAB_IDX_PATH = MAIN_PATH / 'data/vocab_idx.bin'
IDX_VOCAB_PATH = MAIN_PATH / 'data/idx_vocab.bin'

# model path
save_model_path = 'models/'
pb_model_path = 'pb_models/'
keep_checkpoint_max = 1
save_checkpoints_steps = 10

# global
batch_size = 2
train_steps = 10000000
print_info_interval = 10
learning_rate = 1e-2
lr_limit = 1e-2
colocate_gradients_with_ops = True

# Bert
class BertEncoderConfig(object):
  hidden_dropout_prob = 0.1
  attention_dropout_prob = 0.1

  vocab_size = 7819
  embedding_size = 32
  max_positional_embeddings = 30
  hidden_size = 32
  num_hidden_layers = 4
  num_attention_heads = 4
  intermediate_size = 32

  initializer_range = 0.02
  hidden_act = 'gelu'

# Decoder
class DecoderConfig(object):
  unit_type = 'GRU'
  num_units = 32
  forget_bias = True
  tgt_vocab_size = 7819

  dropout = 0.1
  initializer_range = 0.02
  
  sos_id = 1
  eos_id = 2
  max_len_infer = 30