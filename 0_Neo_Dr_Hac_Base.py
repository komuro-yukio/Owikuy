import datetime
import pandas as pd
import tkinter as tk
from tkinter import messagebox as box
from tkinter import ttk
from tkinter import Button
from tkinter import messagebox

root = tk.Tk()
root.title("Dr_Neo_Hac")
root.geometry("1060x600")

lb0 = tk.Label(text='@2024 Komuro Yukiwo',font=("Arial", "5",))
lb0.place(x=970, y=0.6)

a0, b0 = 45,  20
a1, b1 = 45,  60
a2, b2 = 45, 100
a3, b3 = 45, 140

lbt = tk.Label(text='担当')
lbt.place(x=a1, y=b1)

lb1 = tk.Label(text='品ｺｰﾄﾞ')
lb1.place(x=a1+100, y=b1)
lb2 = tk.Label(text='型式')
lb2.place(x=a1+220, y=b1)

lb4 = tk.Label(text='納期')
lb4.place(x=a1+520, y=b1)
lb5 = tk.Label(text='数量')
lb5.place(x=a1+625, y=b1)
lb6 = tk.Label(text='仕切')
lb6.place(x=a1+745, y=b1)
lb7 = tk.Label(text='金額')
lb7.place(x=a1+868, y=b1)


lb8 = tk.Label(text='客先') #客先1
lb8.place(x=a2, y=b2)
lb9 = tk.Label(text='納期') #納期1
lb9.place(x=a2+105, y=b2)
lb93 = tk.Label(text='/') #納期1/
lb93.place(x=a2+168, y=b2)
lbs1 = tk.Label(text='数量') #数量1
lbs1.place(x=a2+215, y=b2)



lb10 = tk.Label(text='客先') #客先2
lb10.place(x=a2+320, y=b2)
lb11 = tk.Label(text='納期') #納期2
lb11.place(x=a2+425, y=b2)
lb113 = tk.Label(text='/') #納期2/
lb113.place(x=a2+483, y=b2)
lbs2 = tk.Label(text='数量') #数量2
lbs2.place(x=a2+530, y=b2)


lb12 = tk.Label(text='客先') #客先3
lb12.place(x=a2+635, y=b2)
lb13 = tk.Label(text='納期') #納期3
lb13.place(x=a2+735, y=b2)
lb133 = tk.Label(text='/') #納期3/
lb133.place(x=a2+793, y=b2)
lbs3 = tk.Label(text='数量') #数量3
lbs3.place(x=a2+845, y=b2)


lb14 = tk.Label(text='備考1') #備考1
lb14.place(x=a3, y=b3)
lb15 = tk.Label(text='備考2') #備考2
lb15.place(x=a3+420, y=b3)


#tk.Entry(validate='focusin') ==> フォーカスが当たった場合に入力制限を受ける


txtt = tk.Entry(width=5) #担当
txtt.place(x=a1+40, y=b1)

txt1 = tk.Entry(width=10) #品ｺｰﾄﾞ
txt1.place(x=a1+140, y=b1)
txt2 = tk.Entry(width=20) #型式
txt2.place(x=a1+255, y=b1)
txt3 = tk.Entry(width=20) #型式2
txt3.place(x=a1+385, y=b1)

txt4 = tk.Entry(width=10) #納期
txt4.place(x=a1+555, y=b1)
txt5 = tk.Entry(width=12) #数量
txt5.place(x=a1+660, y=b1)
txt6 = tk.Entry(width=12) #仕切
txt6.place(x=a1+780, y=b1)
txt7 = tk.Entry(width=15) #金額
txt7.place(x=a1+900, y=b1)

txt8 = tk.Entry(width=10) #客先1
txt8.place(x=a2+35, y=b2)
txt91 = tk.Entry(width=4) #納期1-1
txt91.place(x=a2+140, y=b2)
txt92 = tk.Entry(width=4) #納期1-2
txt92.place(x=a2+180, y=b2)

txts1 = tk.Entry(width=8) #数量1
txts1.place(x=a2+250, y=b2)


txt10 = tk.Entry(width=10) #客先2
txt10.place(x=a2+355, y=b2)
txt111 = tk.Entry(width=4) #納期2-1
txt111.place(x=a2+455, y=b2)
txt112 = tk.Entry(width=4) #納期2-2
txt112.place(x=a2+495, y=b2)

txts2 = tk.Entry(width=8) #数量2
txts2.place(x=a2+565, y=b2)


txt13 = tk.Entry(width=10) #客先3
txt13.place(x=a2+665, y=b2)
txt141 = tk.Entry(width=4) #納期3-1
txt141.place(x=a2+765, y=b2)
txt142 = tk.Entry(width=4) #納期3-2
txt142.place(x=a2+805, y=b2)

txts3 = tk.Entry(width=8) #数量3
txts3.place(x=a2+880, y=b2)


txt16 = tk.Entry(width=60) #備考1
txt16.place(x=a3+40, y=b3)
txt17 = tk.Entry(width=60) #備考2
txt17.place(x=a3+460, y=b3)

v1 = tk.IntVar()
v1.set(0)
rd0 = tk.Radiobutton(root, text='通常手配',value = 0,variable=v1)
rd0.place(x=a0, y=b0)
rd1 = tk.Radiobutton(root, text='先行手配',value = 1,variable=v1)
rd1.place(x=a0+80, y=b0)

v2 = tk.IntVar()
v2.set(0)
rd2 = tk.Radiobutton(root, text='SDK大阪 ',value = 0,variable=v2)
rd2.place(x=a0+175, y=b0)
rd3 = tk.Radiobutton(root, text='SDK東京 ',value = 1,variable=v2)
rd3.place(x=a0+245, y=b0)
rd4 = tk.Radiobutton(root, text='佐野商会',value = 2,variable=v2)
rd4.place(x=a0+315, y=b0)
rd5 = tk.Radiobutton(root, text='三社電機',value = 3,variable=v2)
rd5.place(x=a0+385, y=b0)
rd6 = tk.Radiobutton(root, text='東京ﾊﾟｰﾂ',value = 4,variable=v2)
rd6.place(x=a0+465, y=b0)
rd7 = tk.Radiobutton(root, text='省栄Ｐ',value = 5,variable=v2)
rd7.place(x=a0+535, y=b0)
rd8 = tk.Radiobutton(root, text='東亜無線',value = 6,variable=v2)
rd8.place(x=a0+595, y=b0)
rd9 = tk.Radiobutton(root, text='その他　',value = 7,variable=v2)
rd9.place(x=a0+675, y=b0)
txt0 = tk.Entry(width=20) #その他仕入先名
txt0.place(x=a0+735, y=b0+3)

tree = ttk.Treeview(root)
tree["columns"] = (0,1,2,3,4,5,6,7,8,9,22,23)
tree["show"] = "headings"

tree.heading(0,text="no")
tree.heading(1,text="区分")
tree.heading(2,text="仕入")
tree.heading(3,text="担当")
tree.heading(4,text="品ｺｰﾄﾞ")
tree.heading(5,text="型式")
tree.heading(6,text="型式2")
tree.heading(7,text="納期")
tree.heading(8,text="数量")
tree.heading(9,text="仕切")
#tree.heading(10,text="客先")
#tree.heading(11,text="月")
#tree.heading(12,text="日")
#tree.heading(13,text="数量")
#tree.heading(14,text="客先")
#tree.heading(15,text="月")
#tree.heading(16,text="日")
#tree.heading(17,text="数量")
#tree.heading(18,text="客先")
#tree.heading(19,text="月")
#tree.heading(20,text="日")
#tree.heading(21,text="数量")
tree.heading(22,text="備考1")
tree.heading(23,text="備考2")

tree.column(0, width=2)    #no
tree.column(1, width=2)    #担当
tree.column(2, width=2)    #発注区分
tree.column(3, width=2)    #仕入先
tree.column(4, width=5)    #品ｺｰﾄﾞ
tree.column(5, width=100)    #型式
tree.column(6, width=100)    #型式2
tree.column(7, width=12)    #納期
tree.column(8, width=10)    #数量
tree.column(9, width=10)    #仕切
#tree.column(10, width=8)    #客先1
#tree.column(11, width=3)    #月11
#tree.column(12, width=3)    #日12
#tree.column(13, width=8)    #数量1
##tree.column(14, width=8)    #客先2
##tree.column(15, width=3)    #月21
#tree.column(16, width=3)    #日22
#tree.column(17, width=8)    #数量2
#tree.column(18, width=8)    #客先3
#tree.column(19, width=3)    #月31
#tree.column(20, width=3)    #日32
#tree.column(21, width=8)    #数量3
tree.column(22, width=55)    #備考1
tree.column(23, width=55)    #備考2


i = 0
ent_list = []
ary_list = []
def add():
    global i
    num1 = v1.get()
    num2 = v2.get()
    if num1 == 0:
        txtk_vl = "通常"       #発注区分
    else:
        txtk_vl = "先行"       #発注区分

    if   num2 == 0:
        txts_vl = "SDK大阪"       #発注先
    elif num2 == 1:
        txts_vl = "SDK東京"       #発注先
    elif num2 == 2:
        txts_vl = "佐野商会"       #発注先
    elif num2 == 3:
        txts_vl = "三社大阪"       #発注先
    elif num2 == 4:
        txts_vl = "東京ﾊﾟｰﾂ"       #発注先
    elif num2 == 5:
        txts_vl = "省栄Ｐ"       #発注先
    elif num2 == 6:
        txts_vl = "東亜無線"       #発注先
    elif num2 == 7:
        str = txt0.get()
        str = str.strip()
        if str == "":
            messagebox.showerror('ERROR', '仕入先名を入力して下さい。')
            txt0.focus_set()
            return
        else:
            txts_vl = str       #発注先

    txtt_vl = txtt.get()       #担当
    txt1_vl = txt1.get()       #品ｺｰﾄﾞ
    txt2_vl = txt2.get()       #型式
    txt3_vl = txt3.get()       #型式2
    txt4_vl = txt4.get()       #納期
    txt5_vl = txt5.get()       #数量
    txt6_vl = txt6.get()       #仕切
    txt8_vl = txt8.get()       #客先1
    txt91_vl = txt91.get()     #納期1－1
    txt92_vl = txt92.get()     #納期1－2
    txt10_vl = txt10.get()     #客先2
    txt111_vl = txt111.get()   #納期2－1
    txt112_vl = txt112.get()   #納期2－2
    txt13_vl = txt10.get()     #客先3
    txt141_vl = txt111.get()   #納期3－1
    txt142_vl = txt112.get()   #納期3－2
    txts1_vl = txts1.get()     #数量1
    txts2_vl = txts2.get()     #数量2
    txts3_vl = txts3.get()     #数量3
    txt16_vl = txt16.get()    #備考1
    txt17_vl = txt17.get()    #備考2

    ent_list = [i,num1,num2,txts_vl,txtt_vl,txt1_vl,txt2_vl,txt3_vl,txt4_vl,txt5_vl,txt6_vl,txt8_vl,
                               txt91_vl,txt92_vl,txts1_vl,txt10_vl,txt111_vl,txt112_vl,txts2_vl,txt13_vl,txt141_vl,
                               txt142_vl,txts3_vl,txt16_vl,txt17_vl]
    
    """ List上では先行区分と発注先はnum1,num2として格納される"""

    ary_list.append(ent_list)

    print(ary_list)


    tree.insert("" , 0,values=(i,txtk_vl,txts_vl,txtt_vl,txt1_vl,txt2_vl,txt3_vl,
                               txt4_vl,txt5_vl,txt6_vl,txt16_vl,txt17_vl))



    i = i +1
    
def delete():

    try:        
        rec_id = tree.focus() #レコードのIDを取得
        rec_val = tree.item(rec_id, 'values') #IDを基にデータを取得
        key1 = rec_val[0] #先頭のデータ（no）を取得
        for i in range(len(ary_list)):
            if int(ary_list[i][0]) == int(key1):
                del ary_list[i]
                tree.delete(rec_id)
                break
            else:
                pass
    except:
        box.showinfo("ERROR","No line has been selected.")
    print(ary_list)

    

def print_lst():

    print(ary_list)
    """    
    from pdfrw import PdfReader
    from pdfrw.buildxobj import pagexobj
    from pdfrw.toreportlab import makerl
    from reportlab.pdfgen import canvas
    from reportlab.pdfbase.cidfonts import UnicodeCIDFont
    from reportlab.pdfbase import pdfmetrics
    from reportlab.lib.units import mm
    from reportlab.lib.pagesizes import B5
    from reportlab.lib.pagesizes import portrait  #landscape:横

#    in_file = "C:\\Users\\komur\\Python\\Neo_Dr_Hac\\999_base.pdf"
#    output_file = "C:\\Users\\komur\\Python\\Neo_Dr_Hac\\out555.pdf"
    in_file     = "C:\\Users\\MORIDENSHI\\Desktop\\Python_PGM\\Dr_NEW_HAC\\999_base.pdf"
    output_file = "C:\\Users\\MORIDENSHI\\Desktop\\Python_PGM\\Dr_NEW_HAC\\out555.pdf"

    w, h = portrait(B5)
    cc = canvas.Canvas(output_file, pagesize=(w, h))
    
    font_name = "HeiseiKakuGo-W5"  # フォントの設定

    pdfmetrics.registerFont(UnicodeCIDFont(font_name))
    cc.setFont(font_name, 20)

    page = PdfReader(in_file, decompress=False).pages  # 既存ページ読み込み

#---------------------------------------------------# 1ページ目をオブジェクトに
#---------------------------------------------------# セットする
    pp = pagexobj(page[0])                                                      
    cc.doForm(makerl(cc, pp))
    
    ins  = "神栄キャパシタ"
    in0  = "103"
    in1  = "44183"
    in2  = "TC-300CAS-10(58X74.5)ﾇｷﾋﾝ00000"
    in3  = "図番：ＤＲ－３２３２９１９９"
    in4  = "20241025"
    in5  = "999,999"
    in6  = "999,999.99"
    in7  = "999,999,999"
    in8  = "ナカリキッド"
    in9  = "08"
    in10 = "10"
    in11 = "1,000"    
    in12 = "神港テクノス"
    in13 = "08"
    in14 = "15"
    in15 = "1,000"
    in16 = "日本空調北陸"
    in17 = "08"
    in18 = "20"
    in19 = "1,000"
    in20 = "０１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０" 
    in21 = "０１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０"

#----------------------------------------------------------------------------
## 上段の発注書に値を挿入

## 楕円を描く
    cc.setStrokeColorRGB(0, 0, 0)

    # 楕円挿入位置の指定  x1, y1 = 下から数えて楕円の接する長方形の左上
    # 楕円挿入位置の指定  x2, y2 = 下から数えて楕円の接する長方形の右下
    
    x10 ,y10 ,x20 ,y20 = 120*mm, 242.5*mm, 131*mm, 235.5*mm  #新規
    x11 ,y11 ,x21 ,y21 = 15*mm, 242.5*mm, 45*mm, 235.5*mm  #通常手配       
    x12, y12, x22, y22 = 51*mm, 242.5*mm, 81*mm, 235.5*mm  #先行手配
    x13, y13, x23, y23 = 15*mm, 233.5*mm, 39*mm, 227.5*mm  #新電元大阪
    x14, y14, x24, y24 = 40*mm, 233.5*mm, 64*mm, 227.5*mm  #新電元東京
    x15, y15, x25, y25 = 66*mm, 233.5*mm, 90*mm, 227.5*mm  #省栄プリント
    x16, y16, x26, y26 = 92*mm, 233.5*mm, 116*mm, 227.5*mm  #佐野商会
    x17, y17, x27, y27 = 15*mm, 225*mm, 39*mm, 219*mm  #三社電機
    x18, y18, x28, y28 = 40*mm, 225*mm, 64*mm, 219*mm  #東京パーツ
    
    # 線の太さを指定
    cc.setLineWidth(0.5*mm)

    # 楕円を描画
    cc.ellipse(x10, y10, x20, y20)
    cc.ellipse(x11, y11, x21, y21)
    cc.ellipse(x12, y12, x22, y22)
    cc.ellipse(x13, y13, x23, y23)
    cc.ellipse(x14, y14, x24, y24)
    cc.ellipse(x15, y15, x25, y25)
    cc.ellipse(x16, y16, x26, y26)
    cc.ellipse(x17, y17, x27, y27)
    cc.ellipse(x18, y18, x28, y28)

    # その他仕入先をセット
    cc.setFont(font_name, 8)
    target_x, target_y = 102.5*mm, 237.5*mm  
    cc.drawCentredString(target_x, target_y, ins)  #発行年（基準は中心）

## 作成日をセット ##
    now = datetime.datetime.now()
    yyyy = str(now.year)
    mon   = str(now.month)
    day   = str(now.day)

    cc.setFont(font_name, 8)
    target_x, target_y = 136*mm, 236*mm  
    cc.drawString(target_x, target_y, yyyy)  #発行年

    cc.setFont(font_name, 8)
    target_x, target_y = 152*mm, 236*mm  
    cc.drawString(target_x, target_y, mon)  #発行月

    cc.setFont(font_name, 8)
    target_x, target_y = 161*mm, 236*mm  
    cc.drawString(target_x, target_y, day)  #発行日

#----------------------------------------------------------------------------
##  ## 担当者セット##
    cc.setFont(font_name, 15)
    target_x, target_y = 119*mm, 222*mm  
    cc.drawString(target_x, target_y, in0)  #担当者
#----------------------------------------------------------------------------    
##  ## 品ｺｰﾄﾞ　型式１・２をセット ##
    cc.setFont(font_name, 10)
    target_x, target_y = 20*mm, 207*mm 
    cc.drawString(target_x, target_y, in1)  #HINCD

    target_x, target_y = 39*mm, 207*mm
    cc.drawString(target_x, target_y, in2) #NAME1

    target_x, target_y = 157*mm, 207*mm
    cc.drawRightString(target_x, target_y, in3) #NAME2
#----------------------------------------------------------------------------
##  ## 納期を年月日に分けてセット ##
    nen = in4[0:4]
    tuki = in4[4:6]
    hi = in4[6:8]

    cc.setFont(font_name, 10)
    target_x, target_y = 25*mm, 196*mm
    cc.drawRightString(target_x, target_y, nen) #納期・年

    target_x, target_y = 37*mm, 196*mm
    cc.drawRightString(target_x, target_y, tuki) #納期・月

    target_x, target_y = 48*mm, 196*mm
    cc.drawRightString(target_x, target_y, hi) #納期・日
#----------------------------------------------------------------------------
##  ## 数量・売価・金額をセット ##

    cc.setFont(font_name, 16.5)
    target_x, target_y = 84*mm, 195*mm
    cc.drawRightString(target_x, target_y, in5) #数量

    cc.setFont(font_name, 16.5)
    target_x, target_y = 124*mm, 195*mm
    cc.drawRightString(target_x, target_y, in6) #売価

    cc.setFont(font_name, 16.5)
    target_x, target_y = 169*mm, 195*mm
    cc.drawRightString(target_x, target_y, in7) #金額

#----------------------------------------------------------------------------
##  ## 客先・納期・数量をセット ##

    cc.setFont(font_name, 10)
    target_x, target_y = 55*mm, 182.5*mm
    cc.drawRightString(target_x, target_y, in8) #客先

    cc.setFont(font_name, 10)
    target_x, target_y = 103*mm, 182.5*mm
    cc.drawRightString(target_x, target_y, in9) #納期月

    cc.setFont(font_name, 10)
    target_x, target_y = 111*mm, 182.5*mm
    cc.drawRightString(target_x, target_y, in10) #納期日

    cc.setFont(font_name, 10)
    target_x, target_y = 129*mm, 182.5*mm
    cc.drawRightString(target_x, target_y, in11) #数量

    cc.setFont(font_name, 10)
    target_x, target_y = 55*mm, 174*mm
    cc.drawRightString(target_x, target_y, in12) #客先

    cc.setFont(font_name, 10)
    target_x, target_y = 103*mm, 174*mm
    cc.drawRightString(target_x, target_y, in13) #納期月

    cc.setFont(font_name, 10)
    target_x, target_y = 111*mm, 174*mm
    cc.drawRightString(target_x, target_y, in14) #納期日

    cc.setFont(font_name, 10)
    target_x, target_y = 129*mm, 174*mm
    cc.drawRightString(target_x, target_y, in15) #数量

    cc.setFont(font_name, 10)
    target_x, target_y = 55*mm, 166*mm
    cc.drawRightString(target_x, target_y, in16) #客先

    cc.setFont(font_name, 10)
    target_x, target_y = 103*mm, 166*mm
    cc.drawRightString(target_x, target_y, in17) #納期月

    cc.setFont(font_name, 10)
    target_x, target_y = 111*mm, 166*mm
    cc.drawRightString(target_x, target_y, in18) #納期日

    cc.setFont(font_name, 10)
    target_x, target_y = 129*mm, 166*mm
    cc.drawRightString(target_x, target_y, in19) #数量

#----------------------------------------------------------------------------
##  ## 備考欄をセット ##

    cc.setFont(font_name, 10)
    target_x, target_y = 25*mm, 158*mm
    cc.drawString(target_x, target_y, in20) #備考１
    
    cc.setFont(font_name, 10)
    target_x, target_y = 25*mm, 153*mm
    cc.drawString(target_x, target_y, in21) #備考２

#----------------------------------------------------------------------------
## ---------------------------下段の発注書に値を挿入--------------------------
#----------------------------------------------------------------------------
## 楕円を描く
    cc.setStrokeColorRGB(0, 0, 0)

    # 楕円挿入位置の指定  x1, y1 = 下から数えて楕円の接する長方形の左上
    # 楕円挿入位置の指定  x2, y2 = 下から数えて楕円の接する長方形の右下
    
    x30 ,y30 ,x40 ,y40 = 120*mm, 141*mm, 131*mm, 133.5*mm  #新規
    x31 ,y31 ,x41 ,y41 = 15*mm, 141*mm, 45*mm, 133.5*mm  #通常手配       
    x32, y32, x42, y42 = 51*mm, 141*mm, 81*mm, 133.5*mm  #先行手配
    x33, y33, x43, y43 = 15*mm, 132*mm, 39*mm, 126*mm  #新電元大阪
    x34, y34, x44, y44 = 40*mm, 132*mm, 64*mm, 126*mm  #新電元東京
    x35, y35, x45, y45 = 66*mm, 132*mm, 90*mm, 126*mm  #ミレニアム
    x36, y36, x46, y46 = 92*mm, 132*mm, 116*mm, 126*mm  #佐野商会
    x37, y37, x47, y47 = 15*mm, 123.5*mm, 39*mm, 117.5*mm  #三社電機
    x38, y38, x48, y48 = 40*mm, 123.5*mm, 64*mm, 117.5*mm  #東京パーツ

    # 線の太さを指定
    cc.setLineWidth(0.5*mm)

    # 楕円を描画
    cc.ellipse(x30, y30, x40, y40)
    cc.ellipse(x31, y31, x41, y41)
    cc.ellipse(x32, y32, x42, y42)
    cc.ellipse(x33, y33, x43, y43)
    cc.ellipse(x34, y34, x44, y44)
    cc.ellipse(x35, y35, x45, y45)
    cc.ellipse(x36, y36, x46, y46)
    cc.ellipse(x37, y37, x47, y47)
    cc.ellipse(x38, y38, x48, y48)

    # その他仕入先をセット
    cc.setFont(font_name, 8)
    target_x, target_y = 102.5*mm, 136.5*mm  
    cc.drawCentredString(target_x, target_y, ins)  #発行年（基準は中心）
  
#----------------------------------------------------------------------------
## 日付をセット ##
    
    cc.setFont(font_name, 8)
    target_x, target_y = 136*mm, 134*mm  
    cc.drawString(target_x, target_y, yyyy)  #発行年

    cc.setFont(font_name, 8)
    target_x, target_y = 152*mm, 134*mm  
    cc.drawString(target_x, target_y, mon)  #発行月

    cc.setFont(font_name, 8)
    target_x, target_y = 161*mm, 134*mm  
    cc.drawString(target_x, target_y, day)  #発行日
#----------------------------------------------------------------------------
##  ## 担当者セット##
    cc.setFont(font_name, 15)
    target_x, target_y = 119*mm,120*mm   #223
    cc.drawString(target_x, target_y, in0)  # 担当
#----------------------------------------------------------------------------
##  ## 品ｺｰﾄﾞ　型式１・２をセット ##
    cc.setFont(font_name, 10)
    target_x, target_y = 20*mm, 105.5*mm 
    cc.drawString(target_x, target_y, in1)  #HINCD

    target_x, target_y = 39*mm, 105.5*mm
    cc.drawString(target_x, target_y, in2) #NAME1

    target_x, target_y = 157*mm, 105.5*mm
    cc.drawRightString(target_x, target_y, in3) #NAME2
#----------------------------------------------------------------------------
##  ## 納期を年月日に分けてセット ##
    nen = in4[0:4]
    tuki = in4[4:6]
    hi = in4[6:8]

    cc.setFont(font_name, 10)
    target_x, target_y = 25*mm, 94*mm
    cc.drawRightString(target_x, target_y, nen) #納期・年

    target_x, target_y = 37*mm, 94*mm
    cc.drawRightString(target_x, target_y, tuki) #納期・月

    target_x, target_y = 48*mm, 94*mm
    cc.drawRightString(target_x, target_y, hi) #納期・日   上段との差は「102mm」
#----------------------------------------------------------------------------
##  ## 数量・売価・金額をセット ##

    cc.setFont(font_name, 16.5)
    target_x, target_y = 84*mm, 93*mm
    cc.drawRightString(target_x, target_y, in5) #数量

    cc.setFont(font_name, 16.5)
    target_x, target_y = 124*mm, 93*mm
    cc.drawRightString(target_x, target_y, in6) #売価

    cc.setFont(font_name, 16.5)
    target_x, target_y = 169*mm, 93*mm
    cc.drawRightString(target_x, target_y, in7) #金額
#----------------------------------------------------------------------------
##  ## 客先・納期・数量をセット ##

    cc.setFont(font_name, 10)
    target_x, target_y = 55*mm, 80.5*mm
    cc.drawRightString(target_x, target_y, in8) #客先

    cc.setFont(font_name, 10)
    target_x, target_y = 102.5*mm, 80.5*mm
    cc.drawRightString(target_x, target_y, in9) #納期月

    cc.setFont(font_name, 10)
    target_x, target_y = 110.5*mm, 80.5*mm
    cc.drawRightString(target_x, target_y, in10) #納期日

    cc.setFont(font_name, 10)
    target_x, target_y = 129*mm, 80.5*mm
    cc.drawRightString(target_x, target_y, in11) #数量

    cc.setFont(font_name, 10)
    target_x, target_y = 55*mm, 72*mm
    cc.drawRightString(target_x, target_y, in12) #客先

    cc.setFont(font_name, 10)
    target_x, target_y = 102.5*mm, 72*mm
    cc.drawRightString(target_x, target_y, in13) #納期月

    cc.setFont(font_name, 10)
    target_x, target_y = 110.5*mm, 72*mm
    cc.drawRightString(target_x, target_y, in14) #納期日

    cc.setFont(font_name, 10)
    target_x, target_y = 129*mm, 72*mm
    cc.drawRightString(target_x, target_y, in15) #数量

    cc.setFont(font_name, 10)
    target_x, target_y = 55*mm, 64*mm
    cc.drawRightString(target_x, target_y, in16) #客先

    cc.setFont(font_name, 10)
    target_x, target_y = 102.5*mm, 64*mm
    cc.drawRightString(target_x, target_y, in17) #納期月

    cc.setFont(font_name, 10)
    target_x, target_y = 110.5*mm, 64*mm
    cc.drawRightString(target_x, target_y, in18) #納期日

    cc.setFont(font_name, 10)
    target_x, target_y = 129*mm, 64*mm
    cc.drawRightString(target_x, target_y, in19) #数量

#----------------------------------------------------------------------------
##  ## 備考欄をセット ##

    cc.setFont(font_name, 10)
    target_x, target_y = 25*mm, 56*mm
    cc.drawString(target_x, target_y, in20) #備考１
    
    cc.setFont(font_name, 10)
    target_x, target_y = 25*mm, 51*mm
    cc.drawString(target_x, target_y, in21) #備考２
    
#----------------------------------------------------------------------------

##### 改行 #####
    cc.showPage()
##### 元のPDFを読み込む #####
    pp = pagexobj(page[0])  
    cc.doForm(makerl(cc, pp))

    cc.setFont(font_name, 20)
    target_x, target_y = 20*mm, 106*mm  # 挿入位置(mm指定)
    cc.drawString(target_x, target_y, "改ページ")  #TORICD # 文字列挿入


##### 改行 #####
    cc.showPage()
##### 元のPDFを読み込む #####
    pp = pagexobj(page[0])
    cc.doForm(makerl(cc, pp))

## 

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
    cc.save()    # 保存
    """


tree.place(x=10, y=200, width=1040, height=330)

########################################################
button_del = Button(root, text="remove from List", command=delete)
button_del.place(x=127, y=555, width=105, height=25)

button_add = Button(root, text="add into List", command=add)
button_add.place(x=22, y=555, width=105, height=25)

button_add = Button(root, text="Print out", command=print_lst)
button_add.place(x=232, y=555, width=105, height=25)



########################################################

def rd9_check(event):
    n = txt0.get()
    if n != "":
        v2.set(7)
    else:
        pass

def len_check(event):
    if len(txt4.get()) == 8:
        pass
    else:
        messagebox.showerror('ERROR', '数字８桁で入力して下さい')
        txt4.focus_set()


def name_in(event):
    df = pd.read_csv("code_name.csv", index_col=0)
    c = txt1.get()
    c = int(c)
    txt2.delete(0, tk.END)
    txt3.delete(0, tk.END)
    try:
        namea = df.at[c, 'name1']
        txt2.insert(tk.END,namea)
        nameb = df.at[c, 'name2']
        txt3.insert(tk.END,nameb)
    except:
        box.showinfo("ERROR","May be. There is no code. So you may input Product_name your-self ! ")

def amt_in(event):

    try:
        q = txt5.get()
        q = int(q.replace(",", ""))

        p = txt6.get()
        p = float(p.replace(",", ""))

        txt5.delete(0, tk.END)
        txt5.insert(tk.END,f'{q:,.0f}')        
        txt6.delete(0, tk.END)        
        txt6.insert(tk.END,f'{p:,.2f}')
        txt7.delete(0, tk.END)

        a = q * p
        a = f'{a:,.0f}'
        txt7.insert(tk.END,a)
    except:

        box.showinfo("ERROR","False with Qrt or Price ")



def set_ime_status_win32(hwnd, status=1):
    """日本語入力をonにする(windows用)"""
    """status=1は全角　status=0は半角"""
    import ctypes
    try:
        imm32 = ctypes.windll.imm32
    except FileNotFoundError:
        return

    try:
        himc = imm32.ImmGetContext(hwnd)
        imm32.ImmSetOpenStatus(himc, status)
    finally:
        imm32.ImmReleaseContext(hwnd, himc)


#entry.bind("<FocusIn>",lambda e:set_ime_status_win32(int(entry.winfo_id()))) 全角入力にする


txt0.bind("<FocusIn>",lambda e:set_ime_status_win32(int(txt0.winfo_id()),status=1)) #その他の時　全角
#txt0.bind("<FocusOut>",lambda e:set_ime_status_win32(int(txt0.winfo_id()),status=0)) #その他を抜ける時

txt0.bind("<FocusOut>", rd9_check)

txtt.bind("<FocusIn>",lambda e:set_ime_status_win32(int(txt0.winfo_id()),status=0)) #担当の時　半角

txt4.bind("<FocusOut>", len_check) #納期桁数ﾁｪｯｸ


txt8.bind("<FocusIn>",lambda e:set_ime_status_win32(int(txt8.winfo_id()),status=1)) #客先1の時　全角
txt8.bind("<FocusOut>",lambda e:set_ime_status_win32(int(txt8.winfo_id()),status=0)) #客先1を抜ける時　半角
txt10.bind("<FocusIn>",lambda e:set_ime_status_win32(int(txt10.winfo_id()),status=1)) #客先2の時
txt10.bind("<FocusOut>",lambda e:set_ime_status_win32(int(txt10.winfo_id()),status=0)) #客先2を抜ける時
txt13.bind("<FocusIn>",lambda e:set_ime_status_win32(int(txt13.winfo_id()),status=1)) #客先3の時
txt13.bind("<FocusOut>",lambda e:set_ime_status_win32(int(txt13.winfo_id()),status=0)) #客先3を抜ける時
txt16.bind("<FocusIn>",lambda e:set_ime_status_win32(int(txt16.winfo_id()),status=1)) #備考1の時
txt16.bind("<FocusOut>",lambda e:set_ime_status_win32(int(txt16.winfo_id()),status=0)) #備考1を抜ける時
txt17.bind("<FocusIn>",lambda e:set_ime_status_win32(int(txt17.winfo_id()),status=1)) #備考2の時
txt17.bind("<FocusOut>",lambda e:set_ime_status_win32(int(txt17.winfo_id()),status=0)) #備考2を抜ける時


txt2.bind("<FocusIn>", name_in)
txt1.bind("<Return>", name_in)
txt7.bind("<FocusIn>", amt_in)
txt6.bind("<Return>", amt_in)  #FocusOut, 





#-----Tab_Order-------------------------------------

rd0.focus_set()

new_order = (rd0,rd1,rd2,rd3,rd4,rd5,rd6,rd7,rd8,rd9,txt0,txtt,txt1,txt2,txt3,txt4,txt5,txt6,txt7,txt8,
                               txt91,txt92,txts1,txt10,txt111,txt112,txts2,txt13,txt141,
                               txt142,txts3,txt16,txt17,button_add,button_del)
for widget in new_order:
    widget.lift()

#------------------------------------------









root.mainloop()

















