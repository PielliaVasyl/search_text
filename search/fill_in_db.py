from search.models import TextSegment

from whoosh.index import create_in
from whoosh.fields import *


schema = Schema(book=STORED, chapter=STORED, page=NUMERIC(stored=True), text=TEXT)
ix = create_in("Whoosh_index", schema)



TextSegment.objects.all().delete()

writer = ix.writer()
ts = TextSegment()
ts.text = '''SECOND THOUGHTS
by Carol Moore
Illustrated by Jason Paulhamus
Science fiction is more than just supposition about future science, technology, and encounters with unknown life forms. It is also a metaphor for human nature and our success or failure in how cultures interact.
'''
ts.chapter = 'Before first chapter'
ts.page = 1
ts.book = 'SECOND THOUGHTS'
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'SECOND THOUGHTS'
ts.chapter = 'DAY ONE'
ts.page = 1
ts.text = '''DAY ONE
Tuesday, June 15
     At high noon a large spaceship floated gently down out of a blue sky to land on the front lawn of the White House. It rested motionless for the next five hours while the White House hummed with activity. The President was evacuated and then the military moved in with troops, tanks and helicopters. Stealth fighters roared overhead. Both Congress and the United Nations called emergency sessions as a frightened world held its breath.
     At exactly 5:00 p.m. eastern time, a small door opened in the side of the craft and a human-like creature stepped out.
     As beings go, it wasn't that alarming. About three feet tall, it had a large head atop a small body with two spindly legs. And there were feather-like appendages growing from its head as well as from what could have been a tail if it were a bird. But it moved like a human and wore a one-piece uniform of a gold metallic material that sparkled in the sun. Walking to the nearest soldier, it stopped short, its two unnaturally large eyes blinking twice. Then in perfect English with a high-pitched voice, it said, "Take me to your esteemed leader."
     After much military and political consternation, the request was granted. Standing before the President of the United States, who was seated at his desk in the oval office surrounded by half a dozen secret agents, the little being bowed. "President and Chief Commander, I humbly come to you as ambassador facilitator for an ancient and distinguished race. Please realize that you're dealing with beings of such power that their purpose must be friendly or you'd have already been destroyed in my humble estimation."
     It paused to scratch the base of a head feather. "I myself am Mooba. My kind are respected throughout the universe as the finest of translators. I must tell you that the Xxlepis ship has been moored at the edge of your solar system for a year now while I've been studying your languages and customs on their behalf. I know all there is to know about all of you, in my humble opinion."
     The President smiled halfheartedly, "Should I find that comforting?"
     Mooba brightened, "Of course. Because I'm thorough I rarely make mistakes." He shrugged. "I'll admit to a few, but none that wasn't rectified. I'm sorry to inform you that yours is not the only species I considered for contact on this '''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'SECOND THOUGHTS'
ts.chapter = 'DAY ONE'
ts.page = 2
ts.text = '''planet. There are some others more appealing, but yours is the most intelligent. And yours is also the only species believing themselves in charge."
     The President's eyebrows lifted at such a statement.
     Mooba continued, "For purposes of decorum, tomorrow I will teach you about the Xxlepis." His top feathers suddenly stiffened. "Be forewarned. Although highly evolved intellectually, the Xxlepis are emotionally fragile and quick to perceive imaginary insults if decorum isn't carefully followed. They're quirky that way--easily offended. And if you offend them you will not reap the benefits they can bestow."
     "Fair enough" the President agreed, but his expression was one of puzzlement.
     The conversation was over.
'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'SECOND THOUGHTS'
ts.chapter = 'DAY TWO'
ts.page = 2
ts.text = '''DAY TWO
Wednesday, June 16
     The next day two soldiers were sent to escort Mooba back to the White House, but he wasn't on the spaceship. Instead, when the President with his staff and secret agents arrived at the meeting room, Mooba was already there. Without anyone noticing, he had left the spaceship, slipped through a ring of military, a mob of reporters and White House staff to find the secured meeting room no one had told him about the day before. It unnerved the President and particularly his secret agents.
     Standing at the back of the room Mooba waited for everyone to get settled. Then he abruptly began, "The first thing to do when introduced...is to bow. Some of your human cultures already practice that formality. And the second thing after bowing... is to do nothing." He paused for emphasis. "It's best, Sir President, to allow me to do all the talking, particularly in the beginning. The Xxlepis themselves rarely speak because words to them are sacred. They believe that by saying less, what is said increases in value. So speaking only at the end of a conversation is a sign of respect. Of course, in my humble opinion, that makes for very short conversations." It was hard to tell if Mooba was joking so no one laughed.
     The alien continued. "The Xxlepis find it difficult dealing with other cultures, so they take great care to insulate themselves. In addition to being their translator I serve as a filter to shield their refined sensibilities--but still I must be accurate and complete. Not an easy job, in my humble opinion. The Xxlepis are emotional, you see. Despite all their sophistication, they just want to be loved and they can't handle rejection. I think you humans can appreciate that." He watched as one of the staff arose and walked to a table at the side of the room pouring himself a cup of coffee.
     "What's that?"
'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'SECOND THOUGHTS'
ts.chapter = 'DAY TWO'
ts.page = 3
ts.text = '''     "The President smiled. "It's coffee, a common beverage. And there's also donuts. Would you like some?"
     Mooba's top feathers twitched excitedly. "Certainly." He stepped quickly across the room and to everyone's surprise gulped down a whole carafe of hot coffee. Then he grabbed several donuts. Returning to the front of the room, he noisily smacked his lips. Powdered sugar from the donuts had somehow ended up on his chin. It was a comical sight that everyone politely ignored.
     "That was tasty," he said, "in my humble opinion. Now, let me explain more about the Xxlepis. Having mastered the mysteries of science and technology, they have returned to the arts, particularly their poetry. They are on a quest for new forms of expression. For example, the 20 ways an elephant calls to its young or the 59 words the Eskimos use for snow. Whether or not a language is written or spoken is of secondary importance. The Xxlepis take pleasure in converting all manner of creature communication into just the right word with a precise meaning and contextual flavor to be used in their poetry. So they traverse the universe in search of communication to define new words because, to them, only words have true value. Personally, I think it's because words convey emotions."
     "Speaking of value..." Mooba stopped mid-thought. "Ah... could I have more coffee?"
     "Sir, there's no more coffee," said one of the agents addressing the President.
     The President waved his hand. "Well then, please get another carafe. It'll only take a minute."
     The agent left the room. Through the door, which had not fully closed, squeezed a short, rotund Basset Hound. It went immediately to the President wagging its tail while casting side-glances at Mooba.
     "Hi there, Sally," the President gently stroked the dog's back. "Mooba, this is my dog. She just had puppies four weeks ago. What do you think of her?"
     Mooba was quite interested, particularly when Sally left the President to approach him, her tail still wagging. He bent over so that his face was almost level with the dog's and she licked the sugar off his chin. His head feathers danced wildly. "I like her," he said and then made a noise somewhere between a bark and a whine. It startled everyone in the room, but Sally woofed in response.
     Suddenly, the agent with the coffee appeared. "Here's the coffee, Sir."
     At that point Sally was let out of the room. Mooba drank more coffee, after which he continued instructing the President.
     "As I was saying, concerning value it's things that have no price that are worth the most to the Xxlepis. Things such as honor or knowledge or joy. That's because emotions, or the intangible, offer infinite possibilities for new words of shading and intensity. When a thing has a price, its value is already set, defined
'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'SECOND THOUGHTS'
ts.chapter = 'DAY TWO'
ts.page = 4
ts.text = '''and limited according to the Xxlepis. So instead of price, value for them is in how many words a thing inspires."
     "But as for emotions...the Xxlepis fell in love with the Drugans on the planet Phizell because they're always laughing. They have 32 words for 'giggle'. The Xxlepis were so thrilled with this that they made fools of themselves, showering them with half our gifts." He frowned. "I had an awful time convincing them to leave that planet."
     Rolling his eyes, the little alien continued.
     "Unfortunately, your culture values things more than words. That's what I learned from your television and radio signals. For example, when a commercial says a car has a soul, where does that leave a man? In order to add value to a thing, you've stolen a word meant only for living beings and devalued it. And in devaluing that word you've devalued yourselves. The Xxlepis would never understand and it's better that they not know about it. In my humble opinion."
     Mooba patted a tail feather. "On the other hand, your world's libraries are filled with books and are an endless resource for poetry and great writings. Human beings are capable of deep thought and intense emotions and some have a desire to define them. It is these writings that will appeal to the Xxlepis and they will reward you beyond imagination. As long as they remain on this planet they will bestow gifts, so it's to your benefit to please them. That's all I can say."
     He bowed and the meeting was abruptly over.
'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'SECOND THOUGHTS'
ts.chapter = 'DAY THREE'
ts.page = 4
ts.text = '''DAY THREE
Thursday, June 17
     The introduction of the Xxlepis was set for noon. Although it was an unusually overcast day, that hadn't stopped a huge crowd from forming. At two minutes to 12:00 the President and four secret agents walked slowly up the red carpet and stopped 20 feet from the craft.
     With the opening of a large door, a strange green mist emanated from the craft. Then a long and gently sloped ramp slid out upon which Mooba exited. The murmuring crowd hushed as three figures emerged from behind him. The figures were nearly seven feet tall, rather thin, and covered entirely in grey-green flowing robes and hoods. More than anything they resembled Gregorian monks, but it was how they moved that was startling. Although there was not a breath of wind, their robes rippled fluidly and they appeared to pour across the 20 feet coming to rest alongside Mooba and in front of the President and the agents.
     Mooba's high voice spoke into the multitude of microphones set up by reporters and it sounded over the PA system. "Members of planet earth, I am pleased to introduce you to the Xxlepis. And, they in turn are very pleased to meet you." As he said this the three beings bowed deeply as did the President and his agents.

'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'SECOND THOUGHTS'
ts.chapter = 'DAY THREE'
ts.page = 5
ts.text = '''Mooba continued, "Supreme Commander, President of the United States and all citizens of earth, I am pleased to inform you on behalf of the Xxlepis that today they would like you to accept this gift that they offer you without reservation." Withdrawing something from a hidden pocket, Mooba handed it to the President.
     Accepting the object, which fit into the palm of his hand, the President bowed again. "Thank you."
     Seeing the three Xxlepis nodding from beneath their hoods, Mooba added, "The Xxlepis thank you, too."
     The crowd roared their approval and the first meeting was over.

'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'SECOND THOUGHTS'
ts.chapter = 'DAYS FOUR - TWENTY'
ts.page = 5
ts.text = '''DAYS FOUR - TWENTY
Friday-Sunday, June 18-July 4
     When the gift was examined, scientists were astounded. The President had been handed a container that turned out to hold bacteria from a distant planet. Because these bacteria could manufacture any mineral, the Xxlepis had cultivated and refined it for multiple purposes. Specifically in humans, once ingested the bacteria became symbiotic with living cells and went about curing deficiencies. The resulting good health was miraculous and the closest thing to a fountain-of-youth elixir that humanity had ever experienced. Furthermore, the bacteria were easily reproduced.
     The President wished to reciprocate with a gift of equal value and at Mooba's recommendation commissioned a compendium of sacred writings to be compiled in their original languages. Mooba assured him that as a gift, this would be a delightful surprise for the Xxlepis. It was an ambitious project requiring scholars of every religion and the United Nations was appointed to coordinate it. All nations agreed that no amount of money or effort should be spared to have the gift ready for the next meeting with the Xxlepis.
     Mooba hadn't anticipated the effect the Xxlepis would have on their hosts. Mankind became like children at Christmas. While the Xxlepis's gift of health was reproduced en mass, that was just the beginning.
     Everything had to be Xxlepis-related. To accommodate the demand, manufacturers broke all records (nearly those of physics) to get out a plethora of products. Overnight Gregorian monk's garb became the fashion craze, gray-green the most popular color until Monday when pastel-greens were introduced followed closely by polka dots. People were dressing their babies and pets in robes with cowls. Xxlepis gray-green began showing up on toys, dish ware, buildings. If imitation is the highest form of flattery then the Xxlepis should have been flattered indeed.
     Commercials advertising Xxlepis products had but one theme, life was better with Xxlepis whether you wore Xxlepis clothes or sat on Xxlepis furniture. The inference was, so long as you had Xxlepis you were a somebody with something.
'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'SECOND THOUGHTS'
ts.chapter = 'DAYS FOUR - TWENTY'
ts.page = 6
ts.text = '''Unfortunately, the opposite inference was also true, for without Xxlepis you were considered a nobody with nothing.
     The irony was not lost on Mooba who watched commercialism turn the Xxlepis, a race of beings who loved the nonmaterial, into the biggest name brand of all time.
'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'SECOND THOUGHTS'
ts.chapter = 'DAY TWENTY-ONE'
ts.page = 6
ts.text = '''DAY TWENTY-ONE
Monday, July 5
     When the President and his staff appeared at the spaceship on Monday noon it was before a vastly different-looking crowd. Although a hot July day, the majority was wearing hooded robes, waving signs and holding banners that said, "Xxlepis rocks!"
     This day, upon exiting the craft, the three Xxlepis did not immediately bow. Although their faces couldn't be seen, it appeared that from beneath the cowls they were turning their heads to examine the crowd. Watching them, Mooba's head feathers stiffened noticeably and he frowned.
     This time it was the President who came bearing a gift. The President proudly offered the huge book heavy with gold leafing that one of the Xxlepis gingerly accepted, grasping it with long fingers while the other two Xxlepis stretched forward for a closer look. Their grey-green robes cast a greenish hue over the book.
     "Please accept this gift from mankind," said the President, his voice trembling. "Over 300 of our finest scholars assembled it from our sacred writings."
     Translating, Mooba looked pleased.
     Caught up in the moment and almost as an afterthought, the President added, "Millions were spent. With its parchment and gold leafing, it's the most expensive book ever created."
     Mooba's head feathers quivered the moment the President said the most expensive book ever created. He didn't look pleased. He stopped translating and stared at the President. "Ah, Sir President, in my humble opinion..." he interrupted, but his warning went unheeded.
     "Go on. Tell them," the President urged and Mooba complied.
     The reaction was immediate. Shoving the book back at the President, which he almost dropped, the three Xxlepis, murmuring bubbling-clicking noises, whipped about and swept back up into the spaceship faster than anybody thought they could move. Mooba followed as closely behind as his spindly legs allowed. Pausing at the ship's doorway he turned and shrugged as though apologizing just before the metal door slammed shut with a thud.

'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'SECOND THOUGHTS'
ts.chapter = 'DAY TWENTY-ONE'
ts.page = 7
ts.text = '''     The President and crowd, indeed the whole nation and all of earth were stunned. They felt like children awakening Christmas morning to discover that their presents had been stolen.
     There was no further contact with the Xxlepis although vigorous attempts were made using a PA system as well as radio and television waves and banging on the spaceship doors. Now nobody anywhere talked about anything except the Xxlepis and why they had so abruptly left the gathering. Earth commiserated.
'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'SECOND THOUGHTS'
ts.chapter = 'DAY TWENTY-TWO'
ts.page = 7
ts.text = '''DAY TWENTY-TWO
Tuesday, July 6
     Early Tuesday, without ado, the huge spacecraft gently lifted into the morning air and disappeared.
     It was then Mooba sought admittance to the White House, shocking everyone because they thought he had left along with his alien employers. Escorted to the President's oval office, Mooba's head feathers began to wave as he moaned sorrowfully. "In my humble opinion, my job is just too difficult."
     The President agreed without knowing why as Mooba sat down on a chair. A couple of agents approached to stand behind him. "It's my fault. I thought I'd made you understand, but I was wrong. You meant only to impress when you said the book cost millions to create. But as soon as you gave it a price, in the eyes of the Xxlepis you declared it useless. They were insulted and horrified. They couldn't leave fast enough."
     He hesitated and then glared at the President as if to suggest he did share responsibility. Then Mooba sighed. "It's my humble opinion that they'd never have understood your species anyway."
     "Well then why are you here?" the President was incredulous.
     Suddenly the little alien smiled. "Because unlike the Xxlepis, I don't care about words or meaning or money. Except in the performance of my job, of course. I'm due for a vacation and I'd like a little fun." Before agents could stop him he had jumped up and moved to the President's desk grabbing sour lemon candies from a dish. Popping them into his mouth he made slurping sounds.
     The statement was so ridiculous the President had to laugh. "You mean a permanent vacation? Apparently they're never coming back."
     Mooba grinned knowingly as his head feathers twitched. "On the contrary. I've been with the Xxlepis 120 years and don't you think that if anybody should know what they're doing and why they're doing it, it would be I? That's my humble opinion. As for selecting your species, I've had second thoughts. But don't worry, Sir President, the Xxlepis will be back. Before their ship left I put a puppy on board."
     He popped another sour lemon candy
'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'A Tale of Friendship'
ts.chapter = 'Before first chapter'
ts.page = 1
ts.text = '''A Tale of Friendship
Written and Illustrated by Carol Moore
A special note of thanks to James Poling, the author of Beavers, Their Extraordinary Lives and Curious History, which facts I used for realism and authenticity in the writing of this story.
________________________________________

Author's Note:
Dear reader, while this story is absolutely untrue I make no apologies, for in the imagination of the heart and at the heart of imagination everything is possible and anything could be. It has been said that the world was created in six days and on the seventh day God rested having created all manner of beast and then man. But one animal was not there in the beginning. It was fashioned by the Creator many years later, and this is a story of how it came to be.

'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'A Tale of Friendship'
ts.chapter = 'Chapter One'
ts.page = 1
ts.text = '''Chapter One
________________________________________
Years ago, even before the Indian had set foot in America, there lived a colony of beavers on the banks of a tributary of the Mattawamkeag River in upper Maine. Semi-mountainous, it was a beautiful place with willow, elm and pine trees and plants such as fern and duckweed. The banks of the tributary were dotted with meadows of wild grass created by the beavers in the cutting of trees to build their dam.


The beaver colony was neither large nor small, having three families and ten members, and like all beaver they worked very hard to dam the small river. Although the beavers took occasional breaks, usually for not more than half an hour, one beaver relished sitting at the water's edge deep in thought. He worked harder and faster just so he could sit still longer. If they kept busy with the who and what of things, he found value in the if and why of things -- for hours at a time.

One day in early spring while he was sitting on the bank deep in thought about why trees should shed their leaves in winter, he was distracted by a loud "quack-wack-wack" and "rab-rab-rab". He looked up to see four mallard ducks attacking a smaller one that limped, chasing her from the water onto the bank near him. She struggled to get a foothold, suffering numerous pecks, and he saw anguish in her eyes. It was too much for his sense of fairness. "Stop that," he blurted out.

The ducks ceased their pecking and fell back astonished. They were accustomed to being ignored by beavers so what was this? He glared at them but didn't say anything more, so all but the small one that limped jumped back in the water. She caught her breath before quacking, "Why did you do that?"

The beaver shrugged, "They're always picking on you. I got tired of it."

'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'A Tale of Friendship'
ts.chapter = 'Chapter One'
ts.page = 2
ts.text = '''"Well," she said, "They didn't used to pick on me. But nobody else cares -- not ducks, and certainly not beavers. It's... very curious."

"Curious?"

"Why, yes." The duck began preening her feathers, pretending indifference. "I notice things. If I didn't I couldn't keep out of the way of those hooligans always chasing me. I notice you sit here far more than other beavers do, and...that makes me curious."

The beaver sighed. "Oh, I like that word "curious...curiosity, curiously, curiousness." He rolled the sounds over his tongue like the taste of a tender willow sprig. "I am myself curious about many things. For instance, what is your name?"

"Miena."

The beaver lowered his voice as if they were co-conspirators. "Miena, my name is Dooro. I have a question. I've often wondered about those objects that hang in the sky. Not the clouds, but the round things, that very big bright one during the day, and the dimmer one at night along with all the sparkles. Have you flown there? Can you touch them?"

"Oh, no!" she said. "It doesn't matter how high I fly, they're always farther. I suspect I could fly for ten summertimes and never reach them."

"Really."

Dooro was so impressed Miena flapped her wings momentarily. "Yes, when you fly you do notice a lot of things. Like, did you know there are not just other rivers and lakes like we have right here, but a lake so big it takes weeks, maybe months, to fly across? I've never actually crossed it, but we ducks hear stories from other birds. It tastes salty and strange animals swim in there, like a fish so big it could swallow this pond in one gulp."

The beaver was enchanted. He'd never heard such a thing. He listened in rapt wonder as the duck talked on about seals, dolphins, water spouts and hurricanes. She had an endless supply of information, so their conversation continued for hours punctuated only by the beaver's quick dips into the water. He apologized, explaining that he needed to wet his paws or they developed cracks in the warm spring air. The more Dooro listened the more Miena told until they had talked late into the afternoon and the trees' shadows had became fingers long and thin, and a cool breeze had sprung up.

"I have to go now," said Dooro.

"Me, too," Miena echoed and reluctantly slipped back into the pond.

'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'A Tale of Friendship'
ts.chapter = 'Chapter Two'
ts.page = 3
ts.text = '''Chapter Two
________________________________________
All that week Miena sought Dooro out whenever he rested on the bank. This was partly because the other ducks left her alone when she was with him and partly because he was so happy to see her. They would discuss whatever came to mind, which could be about some difference between ducks and beavers, or the relative threat of such enemies as bear and cougar, or even where they might end up if they flew or swam in one direction forever.


Then one morning Dooro invited Miena to accompany him while he worked. She paddled beside him as he swam gracefully and powerfully closing his forepaws into fists and carrying them close to his chest as he propelled himself forward with webbed hind feet, using his tail as a rudder. When Miena dipped her head underwater for a piece of duckweed Dooro lowered his head too. Instead of ordinary eyelids, his eyelids were transparent. When he closed them it was like looking through windowpanes and he could see her with perfect clarity.

Miena felt exhilarated. She was at home in the water, her feathers providing perfect insulation, and now that she didn't have to worry about other ducks chasing her she could relax and enjoy the surroundings. She loved to paddle against the soft liquid resistance and smell the crisp snap of spring air with its hints of floral bouquet. Even better, by accompanying Dooro she felt she was participating in something important and necessary. She swam alongside him, passing other ducks and beavers, until they had reached the edge of the lake and turned into a narrow canal just wide enough for the beaver's body. She followed him to the end, about 150 feet further, and they climbed out, he shaking his fur and she fluffing her feathers.

Dooro began walking into the forest. Because his short powerful legs made him slow and awkward, he was not graceful on land as he had been in the water, Miena, too, did not glide along but walked with a gimpy waddle. Dooro passed half a dozen trees hesitating momentarily before stopping at the seventh tree to sniff the bark and open his mouth. But unexpectedly the duck sounded an alarm.

"What's wrong?" Dooro exclaimed.

Miena was emphatic. "Not that tree. There's a nest in it."

She lifted her head to point and Dooro saw that there was, indeed, a nest halfway up the tree hidden in the branches. He watched Miena fly to it.

The duck recognized the nest because she had hatched in one just like it. Although ground nests were more common, occasionally some were put in a tree. She found eight olive-green eggs nestled between soft brown feathers and wondered where the parents were. But the nest did feel warm to her feet so she realized the mother

'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'A Tale of Friendship'
ts.chapter = 'Chapter Two'
ts.page = 4
ts.text = '''duck had only recently left and would return shortly. She rejoined Dooro who had already selected another tree.


Using his tail as a stool on which he could sit upright, Dooro gripped the trunk in his forepaws and began chewing the bark of the six-inch willow sapling, dropping chips as he worked. It took only 15 minutes before the tree began to sway on the verge of toppling. Taking one last bite, Dooro slapped his tail on the ground setting off distant thumps and pistol-like pops as other beavers followed suit on ground and water. Even Miena knew this was the beaver's version of "Timber!" an emergency signal that reverberates throughout the beaver colony telling others to seek the safety of water until they are sure no enemies have been attracted by the sounds of a falling tree. Dooro too returned to the canal and waited ten minutes before he got out and began dismembering the branches of the tree and chewing the trunk into pieces about three feet long. Gripping a branch in his teeth he splashed back into the canal, with Miena close behind.

The beaver was tireless and Miena accompanied him as he made 20 trips to the lake and back. He ferried the branches and trunk sections to the dam and with dexterous forefeet and strong jaws pushed, pulled and wove them into the tangled structure. Occasionally another beaver helped him work a particularly large trunk section over the top and rest it at an angle, further buttressing the back of the dam.

Because he was single-minded in his effort Door and Miena talked only occasionally. The beaver had cut down, sectioned and transported two trees to the dam before deciding it was time for a morning break. They sat on the bank watching other beavers still hard at work.

"Were you born here?" asked Miena, nibbling at some watercress that had sprung up at the water's edge.

"Yes," answered Dooro, "In the lodge at the center of the lake." He began rubbing oil on his coat from the scent glands near his tail and using the split toenails of his back feet to comb through his thick mat of underfur. "How about you, where were you born?"

"A lake close by -- one night's flight from here. I left, though. I didn't feel safe there."

"Why not?"

Miena hesitated. "That's where a snapping turtle grabbed me by my foot when I was a duckling. My parents beat at him with their wings until he let me go. If I'd been in deeper water and not so shallow at the time. . ." She shuddered as her voice faded.

"I understand," said Dooro sympathetically. "Aiera the wolf gives us grief, too, but one thing he cannot do is sneak up on us from underwater. That's why we are working so hard right now to keep the water high. Kits are being born. My mother has two new ones."

"Really, where are they? I haven't seen them," exclaimed Miena with interest.

'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'A Tale of Friendship'
ts.chapter = 'Chapter Two'
ts.page = 5
ts.text = '''"Oh, she will bring them out soon. They are not yet a week old, but already she is teaching them how to swim. They learn at the edge of the eating shelf inside the lodge."

"Eating shelf?"

"Oh, I forgot, you have never been inside a lodge, " said Dooro. "We have two levels. The upper level is for sleeping and the lower level slopes to the water and is for eating and a place to dry off. Would you like to see it?"

"Oh, I couldn't disturb your mother and her babies," said Miena.

"No. I will show you my lodge," said Dooro proudly. It's the smaller one near the dam. The back entrance isn't that long."

"Back entrance?

"A tunnel I made from the bottom of the pond to my lodge, maybe 20 feet long. It's a couple of feet wide. I'm sure you could make it."

"I don't know." Miena said. She didn't mind diving, but the image of a dark tunnel unnerved her.

Dooro insisted. "Come on. I will be with you." He coaxed her into the water and over to the area above his tunnel. Then they dove, Dooro leading the way.

As with all beavers, Dooro was endowed with an almost miraculous ability to stay underwater. He had outer ears he could fold shut and flaps of skin in his nose he could close to keep water out. His oversized lungs allowed him to submerge for as long as fifteen minutes and to swim underwater half a mile. When he dove his heartbeat slowed automatically and his body prepared to absorb what to other animals would be poisonous amounts of carbon dioxide. But Miena was not so endowed. Certainly she was able to dive for minutes at a time, but that was under conditions where she could see her surroundings and had immediate access to the surface. Dooro realized there was a problem well before he had reached the entrance to his lodge.

Almost halfway through the tunnel Miena panicked. Pushing against the walls with her webbed toes, she sought to swim faster but only stirred up mud, twigs and debris that clouded the passageway. And once she couldn't see she became disoriented, thrashing about in terror. Sensing trouble, Dooro turned and swam back to her, pushing and guiding her back out of the tunnel with his chest and forepaws until she was into clear water. She stopped floundering and hesitated only a moment before rushing to the surface to draw in deep breaths of air. She made her way to the bank and lay exhausted.

It didn't help that Dooro caught a disapproving glance from his father who was working on the dam. Dooro was overwhelmed with shame. "Miena," he exclaimed. "I really thought you could do it."

"Ohhhh," she gasped. "I'll never do that again. Even if I was chased by 100 turtles I could never, ever enter a tunnel again."

'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'A Tale of Friendship'
ts.chapter = 'Chapter Two'
ts.page = 6
ts.text = '''"I'm sorry." Dooro didn't know what else to say.

"I know you're sorry," Miena reassured him. "You just thought ducks are like beavers -- and we're not. I'm not. Just don't ever mention that horrible place again."

'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'A Tale of Friendship'
ts.chapter = 'Chapter Three'
ts.page = 6
ts.text = '''Chapter Three
________________________________________
Miena didn't hold her unfortunate experience against Dooro. They continued to meet and talk every day, at least for a while, as he was busier than ever. The snow pack was melting and the waters of the tributary swelled, forcing the beaver colony to abandon their lodges, if only temporarily. Dooro explained to Miena that this was actually a good thing because the more water the dam could hold back, the more water there would be to fill new canals and underwater plunge holes so necessary to escape enemies. Now that the trees closest to the lake were gone they had to travel further afield, and each additional canal lined with underwater escape burrows might mean life or death. Through Dooro, Miena came to understand a beaver's passion for dam building.

Along with the increased flow of water and abundant greenery came an explosion of new family members. Besides the coot and merganser ducks with their ducklings, three of the mallard couples were showing off their new broods. Except for their more subdued coloring, Miena thought all the ducklings were adorable miniatures of their parents. For the first time she knew a new yearning and couldn't wait to discuss it with Dooro.

"Do you plan on having a family one day?" she asked the beaver as he lie sunning himself lazily on his back. He flipped to his stomach.

"Yes. I do. A couple weeks ago, as a matter of fact, I was considering it."

Miena was surprised. "You didn't tell me."

"No, I didn't think to. I came across a fresh mound of mud an unfamiliar beaver had put onto a fallen log. She had shaped it into a cone. It smelled... marvelous." He stretched his chin out onto his forefeet and closed his eyes, savoring the memory.

Miena didn't have a clue as to why mud would smell marvelous. "That's.... nice. I have thought about it, too. Not mud, of course -- but having a family. But then..."

Dooro sensed Miena's depression. Knowing she was an outcast from her own kind and unlikely to attract a mate, it occurred to him a distraction was in order. "Look, there's my mother with my brothers."

Sure enough, the mother beaver was swimming across the lake in their direction with her two kits straddling her tail. After passing by a pair of ducks also giving rides to their ducklings, they came right up to Miena and Dooro. The beaver kits
'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'A Tale of Friendship'
ts.chapter = 'Chapter Three'
ts.page = 7
ts.text = '''immediately abandoned their mother and began leaping onto Dooro and then tumbling over one another.

"Boys, behave yourselves," their mother admonished sternly. To Dooro she said, "Your father and I are about to cut down a big spruce tree. Will you watch your baby brothers?"

Dooro's eyes twinkled. He'd already seen Miena fluff her feathers in anticipation. "That will be fine, mother. Maybe I will give them another lesson on dam building."

The mother beaver smiled her beaver smile and nodded serenely, fully trusting her oldest son. She didn't object to Miena. She'd decided it was an odd friendship, but after all, ducks are no threat to beavers. She returned to the water with a gentle slap of her tail and Dooro, Miena, and the kits all followed her as far as the dam.

Once at the dam Dooro began explaining the fine art of dam building. He told them a dam needs to be wider at the bottom than the top. That instead of one big tree being used as a foundation, many saplings and limbs of older trees heavy with brush go into the construction. Then branches are laid side by side in line with the direction of the current and anchored into the mud by rocks and stones, so as not to wash away. With a web of interlaced branches acting like a net, all manner of driftwood and debris are entrapped. Dooro explained that once the foundation is laid, to be watertight the dam needs a plaster of mud, pebbles, and grasses and that this plastering of mud must be done on the upstream side first or it will wash away. And finally, the heaviest logs are added to the dam on the downstream side and pushed against it at right angles for more strength.

Being only three weeks old, Dooro's brothers were hardly attentive. They perked up, however, at the mention of mud. "We want to plaster. Can we do that?" they begged.

It was what Dooro had in mind.

He took them to the bottom of the pond where he showed them how to scoop up armfuls of mud, old leaves and pebbles. His forepaws with their five toes and strong claws were particularly dexterous, and with the support of his paddle-like tail he could walk on his hind legs underwater. Arms full, Dooro actually walked up the side of the eight-foot dam to the surface where he began shoving mud into place with paws and snout. In following his example, the beaver kits were barely successful. Because of their size and underdeveloped coordination, mud melted from their grasp and they quickly discovered stealing Dooro's was an easier way to plaster. He good-naturedly allowed it, although a lot of mud seemed to be drifting back from where it came.

After one dive, Miena was content to stay on the surface and enjoy the young beavers enjoying themselves. She was impressed that animals so young would be so industrious, but eventually their playfulness got the better of them. It was after Dooro's fifth dive that his baby brothers decided mud had a better use. First they began patting it on Dooro, and then themselves, and finally Miena. But the mud war was self-limiting because by that time Dooro had no intentions of gathering

'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'A Tale of Friendship'
ts.chapter = 'Chapter Three'
ts.page = 8
ts.text = '''more mud.

Then they turned to Miena. It occurred to the beaver kits they could pretend to be ducklings and be ferried about. Over Dooro's strenuous objections Miena went along with it, looking decidedly waterlogged, or rather, beaver-logged. She traveled beside the dam towards the bank, figuring to get out once she grew too tired to carry her passengers. They were having a wonderful time, drawing looks of amusement from other ducks as well as beavers.

Suddenly close by there was a noise as loud as a pistol shot -- so loud it could be heard half a mile away. Immediately other loud pops followed, some fainter, as distant beavers sounded the alarm with their tails. Those in the pond reacted by diving or flying, but Miena did neither. One of the kits dove instantly but the other kit seemed confused and was swimming towards the bank. With bone-chilling fear Miena saw Aiera, the dark-gray wolf, loping along the bank in their direction.

Without thinking, and on the pure instincts of a mother duck, she raised a hue and cry as loud as her lungs would permit. "Quack-wack-wack. Quack-wack-wack." Half flying, half pushing the water with her feet she rushed to put herself between the kit and Aiera. The same instant the wolf saw the young beaver he heard and saw the duck. It's automatic that predators attack the weakest and Miena knew instinctively to become vulnerable. She began flapping one wing and bobbing spasmodically, all the while keeping up her "Quack-wack-wack," as though she was in great pain.

The ruse worked. Aiera couldn't resist a wounded duck. He crashed into the pond, water spraying everywhere. His muzzle was only inches away and when he opened wide his mouth Miena saw his fangs. Out of the corner of her eye she also saw the second beaver kit dive to safety. In front of Aiera's eyes she healed instantly, flying up and away to a tree where she could safely watch his reaction.

The thwarted wolf leaped about in the water, sniffing and growling. All the beavers had disappeared and the ducks were either in the trees or had paddled to a safe distance. Aiera's tongue drooled from unanticipated loss and unable to accept defeat, he actually began swimming towards the ducks at the center of the pond. With exaggerated nonchalance they easily outdistanced him and he finally gave up.

Half an hour later the pond's residents were back to doing what they'd been doing before the wolf appeared, except for Dooro, Miena and the kits who stayed close to the family lodge at the center of the pond. While the kits swam and played, Dooro and Miena talked, keeping a wary eye on the bank.

Dooro was in awe. "That was marvelous what you did."

Determined to remain modest, Miena dipped her head in the water several times. Droplets of water rolled and splashed off her back and feathers. "My parents did that for me. It's something we ducks do."

"Well, I still think it was marvelous," insisted Dooro.


'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'A Tale of Friendship'
ts.chapter = 'Chapter Three'
ts.page = 9
ts.text = '''"The place where I live in the wintertime has more than one wolf. They usually live in packs, you know," said Miena changing the subject.

The thought both intrigued and terrified the beaver. "I have never heard of that."

"Well, I've seen it," she assured him.

Miena's worldly knowledge never failed to impress Dooro and after the events of that day, he had even more respect for her. As for the duck, she basked in his respect.

'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'A Tale of Friendship'
ts.chapter = 'Chapter Four'
ts.page = 9
ts.text = '''Chapter Four
________________________________________
The newness of spring changed into the lazy days of summer. Except for an occasional repair of the dam, the beavers were unmotivated to cut any trees. It was a time of abundance for beaver and duck alike because they could now dine on a wide selection of plants. Without leaving the water they feasted on duckweed, water lilies, and watercress. Close by grew ferns, mushrooms, wild grasses, and berries. Miena enjoyed an occasional bug or minnow. Dooro, too, welcomed the change in menu and only occasionally ate willow or aspen, a staple during the winter months. The flourishing plant life of the beaver pond attracted other animals. It was not uncommon to see deer, raccoons, skunk and bear, although the beavers were always nervous when a bear was around. Bears had been known to tear apart beaver lodges.

Meanwhile the ducklings and kits turned into young ducks and beavers. Nature was preparing the ducklings for their winter flight. Early on they had lost their down and begun growing flight feathers. And while the young beavers would not be independent until two years old, by the end of summer at half their adult size, they were fully capable of patching the dam or felling a tree.

Throughout the summer Miena and Dooro continued to have their special conversations. Where Dooro was, there was Miena -- and vice versa. To Dooro, what few beaver conversations he had had, became boring in comparison. As for Miena, well, she had no one else to talk to and grew to prefer it that way.

All too soon the light of day began to shorten and by the end of September the beavers were once again hard at work. With increased cloud cover and colder weather the ducks appeared nervous, watching the sky and looking southward. Their quacking became more frequent and if any one of them took flight, the others watched mesmerized until it had landed. Some of the birds took flight and didn't return. The distant honking of geese and their flying "V" patterns was a bugle call to those with migratory instincts.

The beavers hurried to cut trees for storing in woodpiles underwater. With stones they weighted down successive layers of wood at the bottom of the pond. Because the pond was too deep to freeze all the way to the bottom, this would be their food
'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'A Tale of Friendship'
ts.chapter = 'Chapter Four'
ts.page = 10
ts.text = '''through the winter. As always Dooro worked extra hard and Miena followed him constantly. If he hadn't enjoyed her company so much he might have realized, as did all the other residents of the pond, that at this time of year this was odd behavior. Miena didn't watch the sky or look southward like the other ducks.


It was only after most of the ducks had left the pond and Dooro had begun fortifying his lodge with mud, that he thought to question Miena about it. He was patting the mud carefully onto the dome of his lodge, a master plasterer striving to cover every bit of exposed surface.

"Miena, when are you going to leave with the others?" he said, worry edging his voice.

Miena hesitated. "There's time." Momentarily she tucked her head under her wing, and then shook her feathers.

Dooro persisted. "But almost all the other ducks have already left.

"That's not true. There are ducks left."

Dooro didn't want to argue. He preferred making a suggestion. "Well, at least I hope you plan on leaving with them when they do leave."

Miena looked away and didn't respond. The subject wasn't mentioned again for a while.
'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'A Tale of Friendship'
ts.chapter = 'Chapter Five'
ts.page = 10
ts.text = '''Chapter Five
________________________________________
In a week's time there were no more ducks at the pond, except a forlorn Miena. With even beavers disappearing into their lodges for the winter, Dooro was truly alarmed and determined to straighten it out one way or another.

"Miena, when are you leaving? The ducks are all gone and you know it's time."

The duck's quack was something between a plea and resignation. "I'm not going," she said.

Dooro couldn't believe what he was hearing. "But, why not!"

"I just can't." And then more defiantly, "I don't want to and I won't."

To the pragmatic beaver this violated every instinctual rule. Ducks flew south for the winter and there simply was no other option. Dooro was emphatic. "You can't leave? Well, you can't stay. What would you eat? Where will you live? The pond will be frozen soon."

Miena refused to answer. Instead she turned her back on him and flew off to a tree. The worried beaver didn't know what to do. She was his friend, after all.

'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'A Tale of Friendship'
ts.chapter = 'Chapter Five'
ts.page = 11
ts.text = '''Dooro kept an eye on her all the following week. With each progressive day the now-freezing temperature began to have its effect. The mud the beavers had so carefully applied to their lodges became hard as cement and the pond began to freeze over starting at the shoreline. This was no problem for the beavers who could continue working underwater even in a completely ice-covered pond. Dooro was accustomed to memorizing every air pocket including the ones that always formed along the shore of the pond or the one that formed at the dome of ice above the entrance to his lodge. What he wasn't accustomed to doing was worrying about a duck who had no such defenses against winter's harsh elements. Miena looked more miserable each day.

He thought and thought about how he could help her. He even suggested to Miena that she dive into the pond before it was frozen over so she could seek shelter in his beaver lodge. But this would have meant using the tunnel passageway and Dooro only needed to see the terror in her eyes to know that answer.

Then one morning after it had snowed all night, the frantic quacking of a duck awakened Dooro, comfortably asleep in his lodge. He arrived at the surface of the pond to find Miena stuck in the ice. She had fallen asleep in one of the last clear patches of water and during the night snow and ice had sealed it, trapping her feet. No matter how hard she struggled she couldn't get free and was crying out pitifully.

Without hesitation Dooro began gnawing and clawing at the ice. In his presence Miena ceased crying and lay quiet. It wasn't long before he had freed her.

While he worked, Dooro had resolved to save Miena. He didn't consider it brave or foolish. He only knew that what he planned was against every beaver's deepest instinct. Without acknowledging Miena who followed him, he walked to his lodge and began chewing the outer wall with its mud cement casing. Even with his powerful jaws and his two-inch bottom teeth honed to a knife-like edge, it wasn't easy. The feeling of bitter cold stabbed at his gums until his teeth became numb, but Dooro was single-minded in the determination to vandalize his own fortress. He bit and tore at it for an hour until it was broken open. Then with his snout he nudged in the shaken duck and began immediately making repairs. Even with repair, he realized the protective wall of his lodge would take days to harden again. He finally joined Miena inside.

"Oh, what did you do to your beautiful home?" she said sadly.

With his forepaws Dooro began readjusting the wood shavings. He made a pile for the duck and a pile for himself. "It will be all right," he said. "I've already repaired it. How are you feeling?"

"It's warmer in here," she quacked softly. "Thank you."

With his nose the beaver pushed an elm twig towards the duck. There were several leaves still attached. "Want some?" He asked, trying to sound cheery.

"No thank you." Miena was overcome with gratitude and the last thing she had on her mind was food. She was well aware of how dearly Dooro loved to learn of new things, so she searched her mind for such an item and found it. "Did I ever

'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'A Tale of Friendship'
ts.chapter = 'Chapter Five'
ts.page = 12
ts.text = '''tell you about the enemy of all animals?" she asked.

Dooro's eyes got wide. "All animals. What do you mean?"

Miena lowered her voice. "There's a legend among ducks of an animal whom even our enemies fear. I've never seen it, and my parents never saw it, and no ducks they ever talked to saw it, but nevertheless, there's an animal who uses the rocks of the ground and the limbs of the trees to kill others. It doesn't even need its teeth and it's more deadly than wolf packs or cougars or bears. It kills them all."

"Oh....." Dooro shuddered. "How awful."

"That's not all. Besides eating those it kills, it uses them for a second skin."

"What does this animal look like?"

"It walks on two legs like a bird, but it can't fly. It has arms instead of wings and no tail."

They talked on and on about the strange animal. But while Miena began to relax and enjoy herself, Dooro couldn't ignore a persistent feeling of doom. For good reason. At that very moment Aiera was foraging in their area.

The wolf hadn't eaten in days and with the alluring scent of duck and beaver wafting through the air he followed it eagerly, lifting his muzzle and sniffing often. Crossing the now frozen pond, it didn't take him long to find Dooro's lodge.

Dooro and Miena smelled him before they heard him.

"Dive, Miena!" ordered Dooro.


But the duck, paralyzed with fear, shrank against the wall of the lodge. Dooro knew if he left her she would be killed. Already he could hear Aiera's growling as the wolf tore and scratched at the freshly packed mud and branches. It wasn't long before his head and shoulders broke through.

Dooro, backing up, pushed Miena against the wall and lifted his head to show his teeth. But the stronger and more agile Aiera wasn't the least intimidated. He wriggled and crashed through the barrier leaping on the beaver and pulling him outside. So powerful was Aiera that once he had a solid hold of the beaver's neck he shook him savagely.

The violence of the scene and terrible growls of the wolf awakened Miena from her daze. "Quack-wack-wack." She rushed from the lodge, flapping her wings, doing her best once again to attract Aiera's attention. She finally succeeded, but at what cost. Aiera released the beaver and grabbed Miena by her left wing, breaking it. Then he tossed her into the air to get a deadlier grip.

It was all the chance Dooro needed. Aiera's left back leg came within reach and he bit down as hard as he had ever chomped a willow tree. The bone cracked and Aiera, howling in rage and pain, released Miena. Dooro's attack was totally unexpected and it unnerved the wolf, who was really a coward at heart. He turned

'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'A Tale of Friendship'
ts.chapter = 'Chapter Five'
ts.page = 13
ts.text = '''and fled, using an uneven gait to favor his injured leg.

Unfortunately, for all their bravery both Miena and Dooro were mortally wounded. Their red blood was splattered on the white snow. Dooro collapsed, shivering. "It's cold," he gasped.

Miena, pushing with her webbed feet, struggled to him and laid her good wing over his back like a blanket of feathers. "Is that better?" she asked.

He sighed and closed his eyes. "A little."

'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()

writer = ix.writer()
ts = TextSegment()
ts.book = 'A Tale of Friendship'
ts.chapter = 'Chapter Six'
ts.page = 13
ts.text = '''Chapter Six
________________________________________
The truth is that no matter how noble or terrible our intent, we must face the consequences of our actions. But so strong and pure was Dooro and Miena's friendship that it had not gone unnoticed by the Creator. Such devotion and self-sacrifice are rare and in this case rewarded. Mysteriously, magically, wondrously, Miena and Dooro's wounds were healed -- as surely and quietly as pure love warms a frozen heart. In the twinkling of an eye they were transported halfway around the world to another continent, a new land with new woods and waterways. While transported they were transfigured. Miena lost her feathers, then her wings, which turned into arms, and a thick down of fur enveloped her body. Dooro's nose stretched and spread until it became a bill like Miena's and his body shrank, flattened and grew more compact. In this new land they became a new animal, an animal not quite a bird and not quite a mammal but a bit of both with a broad flat tail and fur softer than a beaver's, with a bill like a duck and "oviparous," which is to say it lays eggs. The Creator looked on his newest creation and saw that it was good.

For one long moment they stared into one another's eyes. Then he cried, "Miena."

She cried "Dooro."


They fell into one another's furry arms, caring not about the how or why, but embracing and tumbling over and over with joy.

That, dear reader, is how the Platypus came to be.


'''
ts.save()
writer.add_document(book=ts.book, chapter=ts.chapter, page=ts.page, text=unicode(ts.text))
writer.commit()
