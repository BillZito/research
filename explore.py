import h5py

file = h5py.File('dataset/log/2016-01-30--11-24-51.h5', 'r')

turns = {}
seq = []
final = []

for idx, ang in enumerate(file['steering_angle']):
  # if idx % 1000 == 1:
  #   print('idx', idx)

  if ang < -180.0 or ang > 180.0:
    time = idx // 100
    if turns.get(time) == None:
      turns[time] = ang
      seq.append(time)

for index in range(0, len(seq) - 1):
  if seq[index] == seq[index + 1] - 1:
    final.append(seq[index])

# print('turns keys', turns.keys())
print('final ranges', final)
# for val in turns:
#   if 
