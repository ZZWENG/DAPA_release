from webbrowser import BackgroundBrowser
import matplotlib.pyplot as plt
import os
import tqdm
import numpy as np
import imageio
import argparse

import soft_renderer as sr

def render(vertices, faces, azimuth=180, camera_distance=2, elevation=20):
    mesh_ = sr.Mesh(vertices, faces)
    transform = sr.LookAt()
    lighting = sr.Lighting()
    rasterizer = sr.SoftRasterizer()
    mesh = lighting(mesh_)
    transform.set_eyes_from_angles(camera_distance, elevation, azimuth)
    mesh = transform(mesh)
    images = rasterizer(mesh)
    image = images.detach().cpu().numpy()[0].transpose((1, 2, 0))
    return image


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--filename-input', type=str,
                    default='smart_120.obj')
args = parser.parse_args()

mesh_ = sr.Mesh.from_obj(args.filename_input)
verts = mesh_.vertices
verts[:,:,1] *= -1
verts[:,:,1] -= 0.4
faces = mesh_.faces
# vertex_textures = np.ones((verts.shape[1], 3), dtype=np.float32)
surface_textures = np.ones((faces.shape[0], 1, 3), dtype=np.float32) * 0.8
mesh_ = sr.Mesh(verts, faces, None, texture_type='surface')

transform = sr.LookAt()
lighting = sr.Lighting(
    intensity_ambient=0.1, color_ambient=[1, 1, 1], 
    intensity_directionals=0.1, color_directionals=[1, 1, 1],
    directions=[1, 0, 0])

rasterizer = sr.SoftRasterizer(image_size=512, background_color=[1,1,1,0], anti_aliasing=True, sigma_val=1e-4, aggr_func_rgb='hard')
writer = imageio.get_writer(f'{args.filename_input}_rotation.gif', mode='I')

loop = tqdm.tqdm(list(range(0, 360, 4)))
camera_distance = 2.2
elevation = 0
azimuth = 0


for num, azimuth in enumerate(loop):
    loop.set_description('Drawing rotation')

    # render mesh
    mesh = lighting(mesh_)
    transform.set_eyes_from_angles(camera_distance, elevation, azimuth)
    mesh = transform(mesh)
    images = rasterizer(mesh, )

    image = images.detach().cpu().numpy()[0].transpose((1, 2, 0))
    writer.append_data((255*image).astype(np.uint8))
writer.close()