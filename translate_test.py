from google_trans_new import google_translator

def main():
    #s = '''After the highs of darkplace it was never conceivable that Holness and Adobye would be able to create anything half as good as garth marengi. Yet i think that man to man in its own right is as good a show (on the good episodes) as darkplace. i cant argue that 2 of the episodes really are'nt that good but the other 4 certainly make up for it. if i had to pick 2 great episodes id go for formula4 driver Steve Pising (pronounced Pissing) and the great Garth Marengi. to already have a bit of understanding of the programme is a real plus as Dean Learner makes many inside jokes but even if you have'nt seen much Dean id recommend this as some of the rants he launches into are genius ie. His argument with Def Lepord over their name. All in All a great show which just misses full marks because of the couple of less funny episodes.'''
    s = '''After the highs of darkplace it was never conceivable that Holness and Adobye would be able to create anything half as good as Garth Marengi.'''
    translator = google_translator()
    translated = translator.translate(s, lang_src='en', lang_tgt='lt')
    print(translated)

if __name__ == "__main__":
    main()