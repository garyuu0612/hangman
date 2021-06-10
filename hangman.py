def hangman (word):
  wrong=0
  stages =['',
           '__________          ',
           '|                   ',
           '|         |         ',
           '|         O         ',
           '|       ／|＼       ',
           '|       ／ ＼       ',
           '|                   ',
           ]
  rletters = list(word)
  #下の式の右辺は、「_」を文字数分だけもつリストをつくる。
  board = ['_'] * len(word)
  win = False
  print("ハングマンへようこそ！")
#stagesは０スタートなので、-1している。
  while wrong < len(stages) -1:
    print('\n')
    msg = '一文字を予想してね'
    char = input(msg)
    if char in rletters:
      #indexメソッドで、charがrlettersの「何番目」かを取得し、それをcindとする。そして、リストのcind番目を入れ替えていく。
      cind = rletters.index(char)
      board[cind] = char
      #複数同じ文字があると、indexはずっと最初の文字しか探さないので、関係ない文字に変えておき、２つ目も探してもらえるようにする。
      rletters[cind] = '$'
    else:
      wrong += 1
    print('\n'.join(board))
    #スライスは右端の値は出力されないので、一つ先の値eを作る
    e = wrong + 1
    print('\n'.join(stages[0:e]))
    if '_' not in board:
      print(' '.join(board))
      print('あなたの勝ち！')
      win = True
      break
  #if no win とは、winがfalseであり、Trueでないことを表す。
  if not win:
    print('\n'.join(stages[0:wrong+1]))
    print('あなたの負け！正解は {}！'.format(word))

hangman("cat")