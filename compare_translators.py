import googletrans

def main():
    translator = googletrans.Translator()

    output = []
    s1 = '''In all of low budget history. this movie has to be one of the worst. True ther are some humorous sides to the movie, but in general it was just plain awful. I just can't understand what person could not out run a bunch of slugs. I mean they have to be one of the slowest creatures on the planet. The only part worth while in this movie is the close up of a slugs attempt to bite the finger of a man. This was rather amusing.
'''
    s2 = '''Thin story concerns two small town brothers and their struggles over family honor. David Morse is the responsible, straight-laced cop and 'good' brother; Viggo Mortensen, the 'bad' boy, is a former soldier and ex-convict. As an actor (particularly in his earliest years), Sean Penn seems to have modulated his performances under the Method. Turning first-time writer and director for this arty, obtuse drama, he works his script and characters out through the same methodical process, slowing the pacing down to a crawl (ostensibly so we can catch every nuance and inflection). This approach might be fascinating if there were three-dimensional characters to care about, but photogenic Morse and Mortensen aren't really convincing as siblings. Worse, we expect more from prominently-billed veterans Charles Bronson and Sandy Dennis, who hardly get a chance to come through with anything interesting. The picture is balky with turgid sequences, a wobbly narrative and confusing editing (always slanted to point up the artistic excesses). Penn's tricks with the camera show off a talented eye, yet they are mostly an irritation. *1/2 from ****
'''
    s3 = '''I had seen this movie when I was a boy (Before WWII) and was surprised that the local library had a copy. Saw it again after some sixty years and forgot how bad it was. This is an example of a movie that was not a "A" movie. No editing, poor script, weak acting and not much directing. Should not even be as high as a "B" Had a laugh at how jaded I've become over the years. Seems to me I thought it was good when I originally saw it.
'''
    s4 = '''Hopper has never been worse as if he felt as this movie is worthy of only a grade B performance and he delivers a rather good one. Outside of Madsen and Hopper the acting is horrid; you've seen better at your local high school. The sound and at times the editing and camera shots are low end of B-movies. The scene with the peeping tom is of movies greatest gratuitous nudity scenes I've ever seen (it doesn't even come close to fitting in the movie). The script was probably a great 10-page outline, but when it comes out to a full-length movie there are more holes in it then the dead bodies Madsen left behind. I do have to say Hopper dressed in a nice suit driving the Hummer had me laughing out loud, but I don't think that was the intent. Yes there is a little style, and Hopper can always draw my interest. However the interesting plot concept never pays off and you are left wondering why you wasted your time watching this.
'''
    s5 = '''If you came into the film with expectations, throw them away now, because no amount of hype will do this film justice.<br /><br />To categorize this film into a single genre would be criminal. It's a spy thriller, has elements of noir, bits and pieces of action, science fiction, and cyberpunk all tied together with a brilliant narrative, mind-bending plot twists, and gorgeous cinematography.<br /><br />A lot of the comments here have centered around it being derivative, both in good and bad ways, of other movies. But as they say, every story cribs from Shakespeare, so once you can get past that, you're in for a hell of a ride.<br /><br />You will need to suspend your disbelief at some points, and while the set never becomes unbelievable, there are portions (read: the elevator) which suffer from a low budget and somewhat cheesy visuals. Don't misconstrue that to mean it's on the same level as cheesy Sci-Fi channel movies, though, because this is on a much higher level.<br /><br />If you're looking for action, you should turn away. This is pure psychology. But if you're willing to sit down and devote a good 90 minutes of your life to a novel cinematic experience, by all means, DO IT NOW! Watch this movie now before it becomes cool to have seen it!'''
    bulk_translations1 = [s1, s2, s3]
    bulk_translations2 = [s4, s5]
    
    output.extend([translation.text for translation in translator.translate(bulk_translations1, src='en', dest='lt')])
    output.extend([translation.text for translation in translator.translate(bulk_translations2, src='en', dest='lt')])
    
    print(len(output))
    print(output)
         

if __name__ == "__main__":
    main()