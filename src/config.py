"""
This file contains definitions of useful data stuctures and the paths
for the datasets and data files necessary to run the code.
Things you need to change: *_ROOT that indicate the path to each dataset
"""
from os.path import join

H36M_ROOT = 'h36m_val'
LSP_ROOT = 'lsp'
LSP_ORIGINAL_ROOT = 'lsp_orig'
LSPET_ROOT = 'hr-lspet'
MPII_ROOT = 'mpii_human_pose'
COCO_ROOT = 'coco'
MPI_INF_3DHP_ROOT = 'mpi_inf_3dhp_full'
PW3D_ROOT = '3dpw'
UPI_S1H_ROOT = '' # not needed for training.
SURREAL_ROOT = ''

# Output folder to save test/train npz files
DATASET_NPZ_PATH = 'data/dataset_extras'

# Output folder to store the openpose detections
# This is requires only in case you want to regenerate
# the .npz files with the annotations.
OPENPOSE_PATH = ''

# Path to test/train npz files
DATASET_FILES = [ {'h36m-p1': join(DATASET_NPZ_PATH, 'h36m_valid_protocol1.npz'),
                   'h36m-p2': join(DATASET_NPZ_PATH, 'h36m_valid_protocol2.npz'),
                   'lsp': join(DATASET_NPZ_PATH, 'lsp_dataset_test.npz'),
                   'mpi-inf-3dhp': join(DATASET_NPZ_PATH, 'mpi_inf_3dhp_valid.npz'),

                   '3dpw': join(DATASET_NPZ_PATH, '3dpw_test.npz'),
                   'seedlings': join(DATASET_NPZ_PATH, 'seedlings_dataset.npz'),
                   'seedlings2': join(DATASET_NPZ_PATH, 'seedlings_dataset_new.npz'),
                   'seedlings_visible': join(DATASET_NPZ_PATH, 'seedlings_dataset_test_visible.npz'),
                   'seedlings_inferred': join(DATASET_NPZ_PATH, 'seedlings_dataset_test_inferred.npz'),
                   'seedlings_overall': join(DATASET_NPZ_PATH, 'seedlings_dataset_test_overall.npz'),
                   'agora_valid': join(DATASET_NPZ_PATH, 'agora_valid.npz'),
                   'agora_validation_keypoints': join(DATASET_NPZ_PATH, 'agora_valid_keypoints.npz'),
                   'agora_test_keypoints': join(DATASET_NPZ_PATH, 'agora_test_keypoints.npz'),
                   'smart': join(DATASET_NPZ_PATH, 'smart.npz'),
                   'gymnastics_darkpose': join(DATASET_NPZ_PATH, 'PSBOjqCtpEU_darkpose_fps3.npz'),
                   'gymnastics': join(DATASET_NPZ_PATH, 'PSBOjqCtpEU_fps3.npz'),
                  },
                  {'h36m': join(DATASET_NPZ_PATH, 'h36m_train.npz'),
                   'lsp-orig': join(DATASET_NPZ_PATH, 'lsp_dataset_original_train.npz'),
                   'mpii': join(DATASET_NPZ_PATH, 'mpii_train.npz'),
                   'coco': join(DATASET_NPZ_PATH, 'coco_2014_train.npz'),
                   'lspet': join(DATASET_NPZ_PATH, 'hr-lspet_train.npz'),
                   'mpi-inf-3dhp': join(DATASET_NPZ_PATH, 'mpi_inf_3dhp_train.npz'),
                   
                   'seedlings_train': join(DATASET_NPZ_PATH, 'seedlings_dataset_train.npz'),
                   'agora_train': join(DATASET_NPZ_PATH, 'agora_train.npz'),
                   '3dpw_train': join(DATASET_NPZ_PATH, '3dpw_train.npz'),
                   '3dpw': join(DATASET_NPZ_PATH, '3dpw_test_new.npz'),  # ft on 3dpw_test
                   'gymnastics_darkpose': join(DATASET_NPZ_PATH, 'PSBOjqCtpEU_darkpose_fps3.npz'),
                   'gymnastics': join(DATASET_NPZ_PATH, 'PSBOjqCtpEU_fps3.npz'),
                   'smart': join(DATASET_NPZ_PATH, 'smart.npz'),
                  }
                ]

DATASET_FOLDERS = {'h36m': 'h36m_train',
                   'h36m-p1': H36M_ROOT,
                   'h36m-p2': H36M_ROOT,
                   'lsp-orig': LSP_ORIGINAL_ROOT,
                   'lsp': LSP_ROOT,
                   'lspet': LSPET_ROOT,
                   'mpi-inf-3dhp': MPI_INF_3DHP_ROOT,
                   'mpii': MPII_ROOT,
                   'coco': COCO_ROOT,
                   '3dpw': PW3D_ROOT,
                   'upi-s1h': UPI_S1H_ROOT,
                   'seedlings': '',  # imgname contains full path, so no need to specify the root.
                   'seedlings2': '',  # imgname contains full path, so no need to specify the root.
                   'seedlings_visible': '',
                   'seedlings_inferred': '',
                   'seedlings_overall': '',
                   'seedlings_train': '',
                   'agora_train': '', 'agora_valid': '', 
                   'agora_validation_keypoints':'', 'agora_test_keypoints': '',
                   '3dpw_train': PW3D_ROOT, '3dpw': '', 'gymnastics': '', 'smart': '', 'gymnastics_darkpose': ''
                }

CUBE_PARTS_FILE = 'data/cube_parts.npy'
JOINT_REGRESSOR_TRAIN_EXTRA = 'data/J_regressor_extra.npy'
JOINT_REGRESSOR_H36M = 'data/J_regressor_h36m.npy'
VERTEX_TEXTURE_FILE = 'data/vertex_texture.npy'
STATIC_FITS_DIR = 'data/static_fits'
SMPL_MEAN_PARAMS = 'data/smpl_mean_params.npz'
SMPL_MODEL_DIR = 'data/body_models/smpl'
UV_MESH_FILE = 'data/smpl_uv.obj'
VPOSER_PATH = 'data/V02_05'