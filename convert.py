'''
run make_frame to convert each image in h5 to video clip

'''
import os
import h5py
import moviepy.editor as mpy
dataset = '2016-04-21--14-48-08'
log = h5py.File("dataset/log/"+dataset+".h5", "r")
cam = h5py.File("dataset/camera/"+dataset+".h5", "r")

# t = 0

def make_frame(t):
  # print('t is', t)
  i = t * 100 + start
  # print('i is', i)
  # log['times'].shape[0]
  if i%100 == 0:
    print("%.2f seconds elapsed" % (i/100.0))
  img = cam['X'][log['cam1_ptr'][i]].swapaxes(0,2).swapaxes(0,1)
  print('image.shape', img.shape)
  # t += .01
  return img

'''
take a set of times for the clip and save it as the cut parts

slice portion of camera based on i

make sure that logs still match up with camera
'''
def cut_clips(ranges):
  #TODO make string flexible to file name and current range
  for r in ranges:
    # print('r is', r)
    new_log = h5py.File('dataset/log2/new_{}_{}.h5'.format(str(r[0]), dataset), 'w')
    new_cam = h5py.File('dataset/camera2/new_{}_{}.h5'.format(str(r[0]), dataset), 'w')
    start = r[0] * 100
    end = r[1] * 100
    
    start_cam = log['cam1_ptr'][start]
    end_cam = log['cam1_ptr'][end]
    # print('start cam', start_cam, 'end cam', end_cam)

    for key in log:
      # TODO: increment by 1 to make end inclusive
      # print('key is', key)
      new_log[key] = log[key][start:end]
      # print('complete one log')

      #TODO: increment by 1 to make end inclusive
    new_cam['X'] = cam['X'][int(start_cam):int(end_cam)]
    # print('complete one cam')

'''
THIS DOES NOT WORK
goal: take 20+ clips in a dir, combines them, and saves
line 72 not complete yet
'''
def combine_clips(dir):
  all_files = os.listdir(dir)
  combo_log = h5py.File('dataset/log2/combo_{}.h5'.format(str(dataset)), 'w')
  print('allfiles_0', all_files[2])
  first_file = h5py.File('dataset/log2/{}'.format(all_files[2]), 'r')
  print('start loop', first_file)
  for key in first_file:
    print('key is', key)
    combo_log[key] = []
    for file_name in all_files[2:]:
      file = h5py.File('dataset/log2/{}'.format(file_name), 'r')
      combo_log[key] = combo_log[key][:] + file[key][:]



if __name__ == '__main__':
  # cut_clips([[16, 18], [18, 20], [20, 24], [26, 28]])
  # combine_clips('dataset/log2/')
  # start = 81000
  # clip = mpy.VideoClip(make_frame, duration=10)
  # clip.write_videofile('test2.mp4', fps=100)

