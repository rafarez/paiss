##############################################################################
# PAISS 2018: Understanding image retrieval representations                  #
# NLE practical session 02/07/2018                                           #
# DEMO                                                                       #
##############################################################################

# Run preliminary imports
import numpy as np
from datasets import create
from archs import *
from tsne import do_tsne
from PIL import Image
import transforms as trf

import argparse
parser = argparse.ArgumentParser(description='Demo')
    
parser.add_argument('--qidx', type=int, default=0, required=False, help='Query index')
parser.add_argument('--topk', type=int, default=5, required=False, help='Showing top-k results')
args = parser.parse_args()

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# load the Oxford5k database
dataset = create('Oxford')
print(dataset)

# initialize architecture and load weights
model = resnet50_rank_DA().to(device)
model.eval()
print(model)

# load the precomputed dataset features
d_feats = np.load('data/features/resnet50-rnk-lm-da_ox.npy')

# Load the query image
img = Image.open(dataset.get_query_filename(args.qidx))
# Crop the query ROI
img = img.crop(tuple(dataset.get_query_roi(args.qidx)))
# Apply transformations
img = trf.resize_image(img, 800)
I = trf.to_tensor(img)
I = trf.normalize(I, dict(rgb_means=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]))
I = I.unsqueeze(0).to(device)
# Forward pass to extract the features
with torch.no_grad():
    q_feat = model(I).numpy()

# Rank the database and visualize the top-k most similar images in the database
dataset.vis_top(d_feats, args.qidx, q_feat=q_feat, topk=args.topk)