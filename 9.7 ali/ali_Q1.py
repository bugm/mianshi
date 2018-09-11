# encoding:utf-8
"""
输入:输入数据包含两行，
第一行，实体列表，多种实体之间用分号隔开，实体名和实体值之间用下划线隔开，多个实体值之间用竖线隔开，所有标点都是英文状态下的，格式如下：
实体名称1_实体值1|实体值2|…;实体名称2_实体值1|实体值2|…;…
第二行，用户的自然语言指令

输出:被标记了关键词的指令。指令中的关键词前后加一个空格被单独分出来，并在后面跟上"/"+实体名称来标记。如果一个实体值属于多个实体，将这些实体都标记出来，并按照实体名称的字符串顺序正序排列，并以逗号分隔。


singer_周杰|周杰伦|刘德华|王力宏;song_冰雨|北京欢迎你|七里香;actor_周杰伦|孙俪
请播放周杰伦的七里香给我听
周杰伦的周杰的孙俪和王力宏与刘德华
唱冰雨首周杰伦的周杰的孙俪和王力宏与刘德华&孙

输出范例:

请播放 周杰伦/actor,singer 的 七里香/song 给我听

第二题：


"""
entities_dict = {}
entity_pieces = set()

e_s = input().strip()
cates = e_s.split(';')
for cate in cates:
  type, entities = cate.split("_")
  entities = entities.split('|')
  for entity in entities:
    if entity not in entities_dict:
      entities_dict[entity] = []
    entities_dict[entity].append(type)

for entity in entities_dict:
  entities_dict[entity].sort()  # 保证type的顺序
  last_s = ''
  for char in entity:
    last_s += char
    entity_pieces.add(last_s)

query = input().strip()
res = ''
last_s = ''
for char in query:
  cur_s = last_s + char

  if cur_s in entity_pieces:
    last_s = cur_s
  else:
    # 输出实体
    if last_s in entities_dict:
      res += ' %s/' % last_s + ','.join(entities_dict[last_s]) + ' '
    res += char
    last_s = ''
if last_s in entities_dict:
  res += ' %s/' % last_s + ','.join(entities_dict[last_s]) + ' '
else:
  res += last_s

print (res)
