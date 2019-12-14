''' Sentiment analysis, for testing purposes '''

from textblob import TextBlob

example_one = TextBlob("A 2017 study found that one in three women here experiences sexual assault by their senior year—a disproportionate figure compared to the one in five statistic reported by the U.S. Department of Health and Human Services’ Office on Women’s Health.")
example_two = TextBlob("While sexual violence is not isolated to our campus, it is troubling to view Columbia’s mismanagement of the problem given how many powerful men with elite pedigrees allegedly don’t care about consent.")
example_three = TextBlob("When Brett Kavanaugh was being confirmed to the Supreme Court last September, I watched all the hearings with grim fascination. I listened as Christine Blasey Ford detailed her alleged attack at the hands of Kavanaugh, horrified but not all that surprised that her alleged attacker was dangerously close to a lifetime appointment to the most powerful court in the country—harking back to Anita Hill’s testimony against Clarence Thomas 27 years before. ")
example_slightly_negative= TextBlob("A woman who says she was subject of a sustained sexual assault by a Labour staffer has for the first time described the harrowing events and the botched internal investigation which followed.")
example_slightly_negative2 = TextBlob("Sarah is one of at least seven people who made formal complaints in relation to the individual, ranging from bullying, intimidation and sexual harassment through to sexual assault.")
example = TextBlob("Haworth responded the following day, and a meeting was arranged. In a private room at Wellington Central Library, Sarah told Haworth and the party’s assistant general secretary, Dianna Lacy, about her encounters with the man, including the full extent of the sexual assault allegations, she said. “I got the sense that [Haworth] was pretty uncomfortable,” she said, though Lacy seemed deeply concerned, and subsequently became the one person within Labour she felt able to rely on.")
example_explicit = TextBlob("In addition to forcing Martina to masturbate and perform oral sex on him, Gregory digitally penetrated and eventually raped her in the church building.")

print(example_one.sentiment)
print(example_two.sentiment)
print(example_three.sentiment)
print(example_slightly_negative.sentiment)
print(example_slightly_negative2.sentiment)
print(example.sentiment)
print(example_explicit.sentiment)