import numpy as np


# # Global constants: pick and place objects, colors, workspace bounds
COLORS = {
    'blue':   (78/255,  121/255, 167/255, 255/255),
    'red':    (255/255,  87/255,  89/255, 255/255),
    'green':  (89/255,  169/255,  79/255, 255/255),
    'orange': (242/255, 142/255,  43/255, 255/255),
    'yellow': (237/255, 201/255,  72/255, 255/255),
    'purple': (176/255, 122/255, 161/255, 255/255),
    'pink':   (255/255, 157/255, 167/255, 255/255),
    'cyan':   (118/255, 183/255, 178/255, 255/255),
    'brown':  (156/255, 117/255,  95/255, 255/255),
    'gray':   (186/255, 176/255, 172/255, 255/255),
}

CORNER_POS = {
  'top left corner':     (-0.3 + 0.05, -0.2 - 0.05, 0),
  'top side':            (0,           -0.2 - 0.05, 0),
  'top right corner':    (0.3 - 0.05,  -0.2 - 0.05, 0),
  'left side':           (-0.3 + 0.05, -0.5,        0),
  'middle':              (0,           -0.5,        0),
  'right side':          (0.3 - 0.05,  -0.5,        0),
  'bottom left corner':  (-0.3 + 0.05, -0.8 + 0.05, 0),
  'bottom side':         (0,           -0.8 + 0.05, 0),
  'bottom right corner': (0.3 - 0.05,  -0.8 + 0.05, 0),
}

ALL_BLOCKS = ['blue block', 'red block', 'green block', 'orange block', 'yellow block', 'purple block', 'pink block', 'cyan block', 'brown block', 'gray block']
ALL_BOWLS = ['blue bowl', 'red bowl', 'green bowl', 'orange bowl', 'yellow bowl', 'purple bowl', 'pink bowl', 'cyan bowl', 'brown bowl', 'gray bowl']

PIXEL_SIZE = 0.00267857
BOUNDS = np.float32([[-0.3, 0.3], [-0.8, -0.2], [0, 0.15]])  # X Y Z
     

# cfg_tabletop = {
#   'lmps': {
#     'tabletop_ui': {
#       'prompt_text': prompt_tabletop_ui,
#       'engine': model_name,
#       'max_tokens': 512,
#       'temperature': 0,
#       'query_prefix': '# ',
#       'query_suffix': '.',
#       'stop': ['#', 'objects = ['],
#       'maintain_session': True,
#       'debug_mode': False,
#       'include_context': True,
#       'has_return': False,
#       'return_val_name': 'ret_val',
#     },
#     'parse_obj_name': {
#       'prompt_text': prompt_parse_obj_name,
#       'engine': model_name,
#       'max_tokens': 512,
#       'temperature': 0,
#       'query_prefix': '# ',
#       'query_suffix': '.',
#       'stop': ['#', 'objects = ['],
#       'maintain_session': False,
#       'debug_mode': False,
#       'include_context': True,
#       'has_return': True,
#       'return_val_name': 'ret_val',
#     },
#     'parse_position': {
#       'prompt_text': prompt_parse_position,
#       'engine': model_name,
#       'max_tokens': 512,
#       'temperature': 0,
#       'query_prefix': '# ',
#       'query_suffix': '.',
#       'stop': ['#'],
#       'maintain_session': False,
#       'debug_mode': False,
#       'include_context': True,
#       'has_return': True,
#       'return_val_name': 'ret_val',
#     },
#     'parse_question': {
#       'prompt_text': prompt_parse_question,
#       'engine': model_name,
#       'max_tokens': 512,
#       'temperature': 0,
#       'query_prefix': '# ',
#       'query_suffix': '.',
#       'stop': ['#', 'objects = ['],
#       'maintain_session': False,
#       'debug_mode': False,
#       'include_context': True,
#       'has_return': True,
#       'return_val_name': 'ret_val',
#     },
#     'transform_shape_pts': {
#       'prompt_text': prompt_transform_shape_pts,
#       'engine': model_name,
#       'max_tokens': 512,
#       'temperature': 0,
#       'query_prefix': '# ',
#       'query_suffix': '.',
#       'stop': ['#'],
#       'maintain_session': False,
#       'debug_mode': False,
#       'include_context': True,
#       'has_return': True,
#       'return_val_name': 'new_shape_pts',
#     },
#     'fgen': {
#       'prompt_text': prompt_fgen,
#       'engine': model_name,
#       'max_tokens': 512,
#       'temperature': 0,
#       'query_prefix': '# define function: ',
#       'query_suffix': '.',
#       'stop': ['# define', '# example'],
#       'maintain_session': False,
#       'debug_mode': False,
#       'include_context': True,
#     }
#   }
# }

# lmp_tabletop_coords = {
#         'top_left':     (-0.3 + 0.05, -0.2 - 0.05),
#         'top_side':     (0,           -0.2 - 0.05),
#         'top_right':    (0.3 - 0.05,  -0.2 - 0.05),
#         'left_side':    (-0.3 + 0.05, -0.5,      ),
#         'middle':       (0,           -0.5,      ),
#         'right_side':   (0.3 - 0.05,  -0.5,      ),
#         'bottom_left':  (-0.3 + 0.05, -0.8 + 0.05),
#         'bottom_side':  (0,           -0.8 + 0.05),
#         'bottom_right': (0.3 - 0.05,  -0.8 + 0.05),
#         'table_z':       0.0,
#       }