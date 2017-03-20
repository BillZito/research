'''
run make file to convert each image in h5 to video clip

'''
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
  # t += .01
  return img

if __name__ == '__main__':
  start = 80000
  clip = mpy.VideoClip(make_frame, duration=10)
  clip.write_videofile('test.mp4', fps=100)

