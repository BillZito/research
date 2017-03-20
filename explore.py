import h5py

# file = h5py.File('dataset/log/2016-01-30--11-24-51.h5', 'r')
# file = h5py.File('dataset/log/2016-01-30--13-46-00.h5', 'r')
# file = h5py.File('dataset/log/2016-01-31--19-19-25.h5', 'r')
# file = h5py.File('dataset/log/2016-02-02--10-16-58.h5', 'r')
# file = h5py.File('dataset/log/2016-02-08--14-56-28.h5', 'r')
# file = h5py.File('dataset/log/2016-02-11--21-32-47.h5', 'r')
# file = h5py.File('dataset/log/2016-03-29--10-50-20.h5', 'r')
# file = h5py.File('dataset/log/2016-04-21--14-48-08.h5', 'r')
# file = h5py.File('dataset/log/2016-05-12--22-20-00.h5', 'r')
# file = h5py.File('dataset/log/2016-06-02--21-39-29.h5', 'r')

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

 
curr_i = 0
while curr_i < len(seq) - 1:
  curr = seq[curr_i]
  count = 0
  inner_arr = []
  while curr_i < len(seq) - 1 and curr == seq[curr_i + 1] - 1:
    if count == 0:
      inner_arr = [seq[curr_i]]
    curr_i += 1
    curr = seq[curr_i]
    count += 1

  if len(inner_arr) == 1:
    inner_arr.append(seq[curr_i])
    final.append(inner_arr)
  
  count = 0
  curr_i += 1

# print('turns keys', turns.keys())
print('final ranges', final)
# for val in turns:
#   if 
