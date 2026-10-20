# Roda cada solução com o EXEMPLO do enunciado e compara com a saída esperada.
# Uso (dentro da pasta solucoes):  python testar.py
import subprocess, sys, glob, os

EXEMPLOS = {
"1025": ("4 1\n2\n3\n5\n1\n5\n5 2\n1\n3\n3\n3\n1\n2\n3\n0 0\n",
         "CASE# 1:\n5 found at 4\nCASE# 2:\n2 not found\n3 found at 3\n"),
"1068": ("a+(b*c)-2-a\n(a+b*(2-c)-2+a)*2\n(a*b-(2+c)\n2*(3-a))\n)3+b*(2-c)(\n",
         "correct\ncorrect\nincorrect\nincorrect\nincorrect\n"),
"1069": ("2\n<..><.<..>>\n<<<..<......<<<<....>\n", "3\n1\n"),
"1110": ("7\n19\n10\n6\n0\n",
         "Discarded cards: 1, 3, 5, 7, 4, 2\nRemaining card: 6\n"
         "Discarded cards: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 4, 8, 12, 16, 2, 10, 18, 14\nRemaining card: 6\n"
         "Discarded cards: 1, 3, 5, 7, 9, 2, 6, 10, 8\nRemaining card: 4\n"
         "Discarded cards: 1, 3, 5, 2, 6\nRemaining card: 4\n"),
"1119": ("10 4 3\n0 0 0\n", "  4  8,  9  5,  3  1,  2  6, 10,  7\n"),
"1167": ("3\nFernanda 7\nFernando 9\nGustavo 11\n5\nMaria 7\nPedro 9\nJoao_Vitor 5\nIsabel 12\nLaura 8\n3\nMaria 4\nPedro 3\nJoao 2\n0\n",
         "Vencedor(a): Fernanda\nVencedor(a): Pedro\nVencedor(a): Pedro\n"),
"1162": ("3\n3\n1 3 2\n4\n4 3 2 1\n2\n2 1\n",
         "Optimal train swapping takes 1 swaps.\nOptimal train swapping takes 6 swaps.\nOptimal train swapping takes 1 swaps.\n"),
"1211": ("2\n12345\n12354\n3\n535456\n535488\n835456\n", "3\n4\n"),
"1259": ("10\n4\n32\n34\n543\n3456\n654\n567\n87\n6789\n98\n",
         "4\n32\n34\n98\n654\n3456\n6789\n567\n543\n87\n"),
"1244": ("4\nTop Coder comp Wedn at midnight\none three five\nI love Cpp\nsj a sa df r e w f d s a v c x z sd fd\n",
         "midnight Coder comp Wedn Top at\nthree five one\nlove Cpp I\nsj sa df sd fd a r e w f d s a v c x z\n"),
"1251": ("AAABBC\n122333\n", "67 1\n66 2\n65 3\n\n49 1\n50 2\n51 3\n"),
"1256": ("2\n13 9\n44 45 49 70 27 73 92 97 95\n7 8\n35 12 2 17 19 51 88 86\n",
         "0 -> \\\n1 -> 27 -> 92 -> \\\n2 -> \\\n3 -> \\\n4 -> 95 -> \\\n5 -> 44 -> 70 -> \\\n6 -> 45 -> 97 -> \\\n7 -> \\\n8 -> 73 -> \\\n9 -> \\\n10 -> 49 -> \\\n11 -> \\\n12 -> \\\n\n"
         "0 -> 35 -> \\\n1 -> \\\n2 -> 2 -> 51 -> 86 -> \\\n3 -> 17 -> \\\n4 -> 88 -> \\\n5 -> 12 -> 19 -> \\\n6 -> \\\n"),
"1258": ("9\nMaria Jose\nbranco P\nMangojata Mancuda\nvermelho P\nCezar Torres Mo\nbranco P\nBaka Lhau\nvermelho P\nJuJu Mentina\nbranco M\nAmaro Dinha\nvermelho P\nAdabi Finho\nbranco G\nSeverina Rigudinha\nbranco G\nCarlos Chade Losna\nvermelho P\n3\nMaria Joao\nbranco P\nMarcio Guess\nvermelho P\nMaria Jose\nbranco P\n0\n",
         "branco P Cezar Torres Mo\nbranco P Maria Jose\nbranco M JuJu Mentina\nbranco G Adabi Finho\nbranco G Severina Rigudinha\nvermelho P Amaro Dinha\nvermelho P Baka Lhau\nvermelho P Carlos Chade Losna\nvermelho P Mangojata Mancuda\n\nbranco P Maria Joao\nbranco P Maria Jose\nvermelho P Marcio Guess\n"),
"1022": ("4\n1 / 2 + 3 / 4\n1 / 2 - 3 / 4\n2 / 3 * 6 / 6\n1 / 2 / 3 / 4\n",
         "10/8 = 5/4\n-2/8 = -1/4\n12/18 = 2/3\n4/6 = 2/3\n"),
"1023": ("3\n3 22\n2 11\n3 39\n5\n1 25\n2 20\n3 31\n2 40\n6 70\n2\n1 1\n3 2\n0\n",
         "Cidade# 1:\n2-5 3-7 3-13\nConsumo medio: 9.00 m3.\n\nCidade# 2:\n5-10 6-11 2-20 1-25\nConsumo medio: 13.28 m3.\n\nCidade# 3:\n3-0 1-1\nConsumo medio: 0.75 m3.\n"),
"1063": ("4\ne t d a\nd a t e\n5\no s t a p\np a t o s\n0\n", "IIIRIRRR\nIIIIIRRR Impossible\n"),
"1077": ("3\nA*2\n(A*2+c-d)/2\n(2*4/a^b)/(2*c)\n", "A2*\nA2*c+d-2/\n24*ab^/2c*/\n"),
"1242": ("SBC\nFCC\nSFBC\nSFBCFSCB\nCFCBSFFSBCCB\n", "1\n1\n0\n4\n5\n"),
"1340": ("6\n1 1\n1 2\n1 3\n2 1\n2 2\n2 3\n6\n1 1\n1 2\n1 3\n2 3\n2 2\n2 1\n2\n1 1\n2 2\n4\n1 2\n1 1\n2 1\n2 2\n7\n1 2\n1 5\n1 1\n1 3\n2 5\n1 4\n2 4\n",
         "queue\nnot sure\nimpossible\nstack\npriority queue\n"),
"1087": ("4 4 6 2\n3 5 3 5\n5 5 4 3\n0 0 0 0\n", "1\n0\n2\n"),
"1236": ("3\n1240000000000000000000000000000000000002342340234Movimento\n", None),
}

aqui = os.path.dirname(os.path.abspath(__file__))
ok = falhou = 0
for arq in sorted(glob.glob(os.path.join(aqui, "*", "*.py"))):
    num = os.path.basename(arq)[:-3]
    if num not in EXEMPLOS or EXEMPLOS[num][1] is None:
        continue
    entrada, esperado = EXEMPLOS[num]
    r = subprocess.run([sys.executable, arq], input=entrada, capture_output=True, text=True, timeout=10)
    if r.stdout.strip() == esperado.strip():
        ok += 1
        print(f"OK     {num}")
    else:
        falhou += 1
        print(f"FALHOU {num}\n--- esperado:\n{esperado}\n--- obtido:\n{r.stdout}{r.stderr}")
print(f"\n{ok} ok, {falhou} falharam")
