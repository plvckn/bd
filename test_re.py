import re
import json
import pprint
import time

def main():
    s = '''
    <!DOCTYPE html><form method=post><textarea name=tekstas rows=15 cols=75>Vienas iš pirmųjų požymių, galinčių įspėti apie aukštą kraujospūdį, yra netolygios ir siauros kraujagyslės.</textarea><br><input type=radio name=tipas value='anotuoti' checked> <B>Pateikti 
    vieną tikėtiniausią variantą</b><input type=radio name=tipas value='lemuoti'> <b>Pateikti visus galimus variantus</b><br><input type=radio name=pateikti value='LM' checked> Lema + gramatinės pažymos <input type=radio name=pateikti value='L'> Tik lema  <input type=radio name=pateikti value='M'> Tik gramatinės pažymos <br><input type=submit name=veiksmas value='Rezultatas puslapyje'><input type=submit name=veiksmas value='Rezultatas faile'></form>&lt;word=&quot;Vienas&quot; lemma=&quot;vienas&quot;/&gt;<br>
    &lt;space/&gt;<br>
    &lt;word=&quot;iš&quot; lemma=&quot;iš&quot;/&gt;<br>
    &lt;space/&gt;<br>
    &lt;word=&quot;pirmųjų&quot; lemma=&quot;pirmas&quot;/&gt;<br>
    &lt;space/&gt;<br>
    &lt;word=&quot;požymių&quot; lemma=&quot;požymis&quot;/&gt;<br>
    &lt;sep=&quot;,&quot;/&gt;<br>
    &lt;space/&gt;<br>
    &lt;word=&quot;galinčių&quot; lemma=&quot;galinčius&quot; status=&quot;galimas&quot;/&gt;<br>
    &lt;space/&gt;<br>
    &lt;word=&quot;įspėti&quot; lemma=&quot;įspėti(-ja,-jo)&quot;/&gt;<br>
    &lt;space/&gt;<br>
    &lt;word=&quot;apie&quot; lemma=&quot;apie&quot;/&gt;<br>
    &lt;space/&gt;<br>
    &lt;word=&quot;aukštą&quot; lemma=&quot;aukštas&quot;/&gt;<br>
    &lt;space/&gt;<br>
    &lt;word=&quot;kraujospūdį&quot; lemma=&quot;kraujospūdis&quot;/&gt;<br>
    &lt;sep=&quot;,&quot;/&gt;<br>
    &lt;space/&gt;<br>
    &lt;word=&quot;yra&quot; lemma=&quot;būti(yra,buvo)&quot;/&gt;<br>
    &lt;space/&gt;<br>
    &lt;word=&quot;netolygios&quot; lemma=&quot;netolygus&quot;/&gt;<br>
    &lt;space/&gt;<br>
    &lt;word=&quot;ir&quot; lemma=&quot;ir&quot;/&gt;<br>
    &lt;space/&gt;<br>
    &lt;word=&quot;siauros&quot; lemma=&quot;siauras&quot;/&gt;<br>
    &lt;space/&gt;<br>
    &lt;word=&quot;kraujagyslės&quot; lemma=&quot;kraujagyslė&quot;/&gt;<br>
    &lt;sep=&quot;.&quot;/&gt;<br>
    &lt;p/&gt;<br>
        
    '''
    word_pattern = 'word=&quot;(.+?)(?=&quot)'
    lem_pattern = 'lemma=&quot;(.+?)(?=\(|&quot;)'
    words = re.findall(word_pattern, s)
    lemmas = re.findall(lem_pattern, s)
    print(words)
    print(lemmas)
    
    word2lemma = dict(zip(words, lemmas))
    testload = {}
    print(word2lemma)
    with open('testdictionary.txt', 'w', encoding='utf-8') as w:
        w.write(json.dumps(word2lemma))
    with open('vocab_lemmas_0.txt', 'r', encoding='utf-8') as r:
        testload = json.load(r)
    time.sleep(3)
    print(testload['yra'])

if __name__ == "__main__":
    main()
