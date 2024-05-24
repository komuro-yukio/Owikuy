import datetime

def insert_text_output_pdfrw():
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


insert_text_output_pdfrw()



#----------------------------------------------------------------------------
##  ## 区分に〇を描画 ##
#    cc.circle(800, 580, 7) ## サンプル
#    cc.circle(786, 580, 7) ## 返品
#    cc.circle(772, 580, 7) ## 値引
#    cc.circle(758, 580, 7) ## 値上
#----------------------------------------------------------------------------

