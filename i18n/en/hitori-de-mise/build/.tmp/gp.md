## Introduction

This book is a record as of January 2026. Some of the ways I run the shop, and some of the names and specifications of the AI tools, have changed since then. The sequel, *Built for Our Bar*, picks up the story.

### Why a Former Systems Guy Is Talking to AI in a Basement Restaurant

Thank you for picking up this book.

*One Person Runs the Shop, and AI Showed Up Beside Me.*

When you see that title, some of you may think, "That's exactly me." Others may wonder, "What does it mean for AI to show up beside you?"

This is not a technical book about difficult programming. It is a book for people like you, restaurant owners who stand in the kitchen every day, do the prep, and are always busy with customers.

Let me tell you a little about myself.

I now run a small restaurant in the basement of a building in Higashi-Nakano *(a residential neighborhood in western Tokyo, just west of Shinjuku)*, Tokyo.

It has two faces. By day, it is a specialty shop for hamburger curry fragrant with spices. By night, it is a referral-only dining bar serving a daily set meal and drinks.

▼ Quatre Epice Hamburger Curry (Instagram)

<https://www.instagram.com/quatre.epice.hamburg.curry/>

![Quatre Epice Hamburger Curry (Instagram)](images/_web/fig-01.png)

▼ Referral-only bar "Tamuro" (Instagram)

<https://www.instagram.com/tamuro.higashinakano/>

![Referral-only bar "Tamuro" (Instagram)](images/_web/fig-02.png)

It is a cozy space with just 11 counter seats and 8 seats on a raised tatami platform.

But we do more than serve food.

We hold a wine event every other week, and once a month we plan a cooking class or a special course-meal day. Even in a cramped basement, we are busy and on the move every day.

This year marks my twelfth year running the shop.

Before that, I worked as a company employee. My work was "systems planning" and "solution architecture."

When I say that, people sometimes respond, "So you were someone who developed impressive systems." That is not actually the case.

What I did was not write difficult program code. I listened to what people on the front lines wanted, conveyed it accurately to IT vendors (development companies), and got it built. I was a "coordinator." In Japan, this position is known as a "systems guy."

The frontline staff wished, "I want my work to be easier." The engineers said, "We need logically defined requirements."

My job was to stand between them, interpret each side's language, and guide everyone to the goal.

That is why I understand the inconveniences and worries of people like you, the ones who use systems, and I also understand a little of what the IT side is thinking.

I left the company twelve years ago and opened my own shop. Since then, I have faced the same worries you do.

Prep that never ends, labor shortages, anxiety about attracting customers, and management decisions I carry alone...

Of course, when it gets busy, I sometimes get help from reliable part-timers and contract staff.

But they are, after all, partners for "tasks."

There is no one I can consult about heavy "management decisions," such as "How do I handle cash flow next month?" or "Should I bet on this new menu item?"

I worry, decide, and take full responsibility. In that sense, I have always been "running the shop alone." And the one who sat beside me, as a confidant for the lonely "me as a business owner," was AI.

Into this situation came generative AI, and in particular a partner called "Google Gemini."

The "coordination" I once did between "the front line" and "IT vendors," I now do myself between "the shop's problems" and "AI." And I realized something.

You do not need to memorize the spelling of difficult programming languages (such as Python).\
The AI knows that. But the blueprint of "what you want done, and in what order" is something only a human can draw.\
What I built up as a systems guy was exactly this "ability to translate what the front line wants into logical steps."\
In this book, I will share not only how to operate AI, but also this "logical instinct for getting AI to work (systems thinking)," holding nothing back.\
Once you have this, you can go from "zero knowledge" to "the best client there is."

※ Let me be honest about one thing here.

I am a former systems guy. But in the AI uses introduced in this book, there were actually almost no moments when my previous job's knowledge directly helped.

What helped was not "the skill of writing programs."\
It was only "the habit of turning the front line's vague frustrations into words that have an order."

And this habit is not a special talent.\
It is "a sense that any owner who runs a shop every day already has."

In this book, I will deliberately separate what only I could do\
from what you can copy exactly, starting today.

## Chapter 1: Concepts - AI Agents, the New Kind of Employee

~ Hire AI as a "work partner," not a "sounding board" ~

### 1-1. The Limits of the Solo Owner, and Misunderstandings About AI

Running an independent restaurant like ours is a constant race against time. Prep, cooking, serving, checkout, cleaning... all of it has to be handled by one person, or a small staff.\
Even if we hire staff, we independent owners are in effect running a "one-person operation."

That is because we do not have "store managers" or "trainers" the way big chains do.

You cook while giving instructions to the floor staff, teach the new hires, and manage the schedule.

All of this "mental processing" is concentrated in one person: you, the owner.

You may get more hands, but you still have only one head. That is exactly why you need AI to support that "head."

"If only I had one more good staff member..."

You must have that thought many times a day.

When I say, "Let's use AI," many owners answer like this:

"You mean ChatGPT? I tried it, but all it does is write text, right? It's no use for work on the floor."

In fact, there is a big misunderstanding here.

Most of the AI we have touched so far has been a "chatbot (a sounding board)." But what the latest AI, starting with Google Gemini, is aiming for now is the form of an "AI agent (a work partner)."

The two look alike but are different things. Let's compare them using a concrete job.

### 1-2. From "Dictionary" to "Staff Member"

Say, for example, you want to make a poster for a shop event.

With the AI of the past (a chatbot):

If you ask, "Tell me how to make a poster," the AI explains the steps like a dictionary or textbook: "Keep the catchphrase short," "Choose the colors like this."

But the one who actually works with their hands to make the poster is you. Your knowledge has grown, but your working time has not shrunk.

With the AI of the future (an AI agent):

You simply instruct, "Make a poster."

Then the AI thinks for itself to achieve the goal. It comes up with the catchphrase, generates the background image, and even proposes the layout.

Like an excellent staff member, it uses tools, plans, and carries out the work on its own.

What we want is not an advisor who states the obvious, but a partner who sweats beside us.

※ In this book, I will affectionately call this reliable partner (generative AI such as Google Gemini) the "deputy manager (AI)."

※ In this book I use "Google Gemini," which I mainly use, as the example, but most of the ideas introduced here can be reproduced in almost the same way with other generative AI such as ChatGPT and Claude.

What matters is not the name of the tool, but "the attitude of treating AI not as a sounding board, but as a partner you can hand work to."

### 1-3. "Multimodal" Is What Will Save Restaurants

There is one more keyword that is critically important in running a restaurant. It is "multimodal."

It is a somewhat technical word, but the meaning is simple.

It means "being able to understand multiple kinds of information at once: not only text (reading and writing), but also images (seeing and drawing) and audio (listening and speaking)."

Conventional AI could understand only "words." But a restaurant floor does not run on "words" alone.

- What the food left in the refrigerator looks like

- Handwriting on order slips

- The voices of customers and the mood of the room

- The label design on a wine bottle

All of these are "non-verbal information" that is a hassle to put into words.

The deputy manager (AI) can recognize these just as a human does.

If you take a photo of the inside of your refrigerator with your phone and show it, the AI recognizes, "Ah, you have extra of this vegetable and that meat," and can come up with a menu from there.

In other words, today's AI is "an excellent deputy manager who can see, hear, and speak."

※ But I do not want you to misunderstand one thing.\
AI is better at saying things that sound plausible than at saying things that are correct. For image recognition, numbers, dates, and proper nouns,\
please use it on the premise that a human always does the final check.

The reason AI works well in this book is\
that I "don't hand everything over, and always check on site."

### 1-4. Back Up Your "Gut Feeling" with Data

Big chain stores have enormous amounts of POS register data and marketing teams.

We independent shops, on the other hand, have your "gut feeling" and "experience" as the owner. This is the strongest weapon, but it can sometimes become self-satisfied or leave you uncertain.

So let's add a "deputy manager."

Have the AI compare your intuition (gut feeling), "I think customers will love this dish," against "past sales data" and "trend information."

That way you can keep the "warmth" and "individuality" that only an independent shop has, and still run a strong business grounded in data.

## Chapter 2: Fundamentals - "Vibe Coding" from Zero Knowledge

~ Programs are not something you "write." They are something you "have AI build by talking to it." ~

### 2-1. Nobody Reads a "Long LINE Message." The Magic of a "Diagram" That Takes 30 Seconds

Saying "build a system with AI" may still feel like a bit of a high hurdle.

So let's start with a more familiar "way to use AI" that you can use right away, starting today.

It is a revolution in "giving instructions to your staff."

Many of us owners use LINE *(Japan's most widely used messaging app)* to contact staff.\
I usually run the shop with a limited number of people, and during busy service there is no time to give instructions calmly.

So announcements inevitably depend on LINE messages after closing.

But it is extremely hard to convey, with words alone, the image of "this is how I want it done" that exists only in my own head to less experienced staff or to the occasional helper.

That is where the "long LINE message" comes from.

The more carefully you try to explain, the longer the text gets, and as a result...

"Oh, sorry, I didn't read that far."

"It was all text, and I couldn't tell which part was important."

Don't mistakes like these happen on your floor?

They did for me too.

One day, for an app I was developing, I tried to ask a staff member to take "photos of ingredients."

The conditions were a bit complicated, so the instructions I typed on my phone turned into a long message like this.

![The long LINE message I actually sent to the staff, typos included](images/_web/fig-03.jpg)

Even when they see this, busy kitchen staff will skim it with "So basically I just take photos, right?" and miss the specifications for "angle" and "container orientation."

But I have no time to open PowerPoint, line up shapes, and make an instruction sheet.

So I fed this text as it was into AI (an AI tool such as Manus, or Gemini) and asked:

"Summarize the content of this text on one slide, as a 'work instruction sheet' that staff can understand at a glance."

### 2-2. AI Is an "Excellent Translator"

After a few seconds of waiting, what the AI produced was a surprisingly easy-to-understand "diagram slide."

![The "Data Collection and Photography Work Instructions" slide automatically generated by AI](images/_web/fig-04.jpg)

I designed nothing. I only said, "Here's the text, summarize it."

From my rambling text, the AI instantly understood "what is important" and "how it should be categorized," and "translated" it into a layout humans can grasp intuitively.

### 2-3. Freedom from the "Stress of Not Getting Through"

I pasted this image into LINE and sent it.

The effect was immediate.

The staff member asked no questions, and sent back perfect photo data in "portrait orientation" with "3 angles" on the first try.

Until then, I had been irritated with staff, thinking "Why won't they read it?" and had worried, "Maybe I'm just explaining badly."

But the one to blame was neither the staff nor me. It was "communication with text alone."

This experience changed how I see AI.

AI is not only a tool for "creating from scratch" new text and images.

It is "a tool that 'converts' the 'words that don't come across well' that we have into a form that reaches the other person."

### 2-4. "Vibe Coding," a New Kind of Dialogue

Once you are used to talking with AI, next comes "building tools" at last.

You may think, "Programming is impossible for me," but don't worry.

Right now, among engineers, a term called "vibe coding" is a hot topic.

It is a method in which, instead of humans writing difficult code, you build a system by talking with AI as if matching "vibes" (feel and mood).

Sota Fujii, the shogi Meijin (title holder), named "vibe coding" as something they got into this year, in 2025. Even someone from the shogi world, which seems completely unrelated to building systems, reportedly tells AI what they want in Japanese and builds handy tools.

By talking with AI, we too can build systems without specialized knowledge.

All you use is "Japanese." When you say, "I want it to work like this" or "This part is hard to use," the deputy manager (AI) writes the code behind the scenes.

In other words, you do not need to become a "programmer."

You just need to become the "site supervisor" who gives instructions to an "excellent engineer (AI)."

### 2-5. Your Shop's "Complaints" Make the Strongest Prompts

Instructions to AI (prompts) do not need to be fancy words.

The strongest prompt I discovered is "your shop's 'inconveniences' and 'frustrations,' in other words, your complaints."

- "It's a pain to do this calculation every day."

- "I don't want to resize images by hand."

For AI, these are perfectly good "development requirements."

A feeling like "I hate this" draws out a concrete solution more easily than a goal like "I want to do this."

### 2-6. An Error Is Not a "Failure." It Is the "Start of a Dialogue."

When you start making something with AI, you will surely run into an "error."

But in vibe coding, an error is not a failure.

It is "the signal that a game of catch with the AI has begun."

Even between humans, it is rare for your intent to come across perfectly the first time.

When the AI gives an error, just brush it off lightly with "Ah, I didn't get through," and ask back, "No, what I want is this."

Keep the rally going without giving up. If you can do just that, even you, with zero knowledge, can surely build "a system that is yours alone."

### 2-7. Dramatically Boost Efficiency with "Physical Buttons" - Using a Sub-Keyboard

In vibe coding, the most important thing is "being particular about input."

The faster your conversation with AI gets, the less your thinking stops, and the faster development moves. Conversely, if you fumble over input, even a great idea can vanish.

Earlier I told you, "When an error appears, the right move is to take a screenshot and paste it."

But pressing [Windows] + [Shift] + [S] (Mac: [Cmd] + [Shift] + [4]) dozens of times a day, selecting an area with the mouse, going back to the Gemini screen, and pressing [Ctrl] + [V] (Mac: [Cmd] + [V])...

Honestly, it tires your fingers, doesn't it?

So what I introduced was a "6-button sub-keyboard."

It is a small, Chinese-made keyboard that costs a few hundred to about a thousand yen, which comes up when you search for "programmable keyboard" on Amazon or similar sites.

![A photo of the 6-button sub-keyboard I use](images/_web/fig-05.jpg)

I have assigned the following shortcuts to these six buttons.

1.  Launch screenshot

2.  Select all (Ctrl + A; Mac: Cmd + A)

3.  Copy (Ctrl + C; Mac: Cmd + C)

4.  Paste (Ctrl + V; Mac: Cmd + V)

5.  Enter (send)

6.  (Spare)

That's all. But the effect is dramatic.

An error appears.

↓

With my left hand, I tap "Button 1 (screenshot)."

↓

I select the area, then tap "Button 4 (paste)" on the Gemini screen.

↓

Tap "Button 5 (send)."

All of this takes just 2 seconds.

You don't need to remember keyboard shortcuts or move your fingers in complicated ways.

You can throw information at the AI as if operating a game controller.

As you will see in later chapters, when you fix the source code the AI outputs, select all (Ctrl + A), copy (Ctrl + C), and paste (Ctrl + V) let you rerun it right away, which is handy.

Before you study advanced programming knowledge, please try getting this one small device first.

Physically eliminating the "hassle of input." That is the surest shortcut to speeding up conversations with your AI partner.

## Chapter 3: Practice 1 - Automating Creative Work and Attracting Customers

~ "Paste a screenshot and hand it all over" turned out to be the strongest development method ~

### 3-1. Trial and Error to Erase the "AI Look" (LINE Stickers)

Having grown used to dialogue in text (vibe coding), I decided to take on "image generation" at last.

For practice, I chose making "LINE stickers," which can also help build fans for the shop.

But the "smooth, CG-like pictures" typical of AI-generated images do not suit the atmosphere of my shop.

What I was aiming for was "a retro, 1980s-style flat design with a hand-drawn feel, keeping the texture of crayon and brush."

From here began a long "dialogue" between me and the deputy manager (AI).

At first, I started with characters of "two boys and a Shiba Inu."

"Give me 25 everyday conversation patterns."

"Make the line thickness random, like brushstrokes."

One by one, as if giving revision instructions to a human illustrator, I patiently taught it the taste I liked.

![Illustrations generated for LINE stickers](images/_web/fig-06.jpg)

### 3-2. The Bold Request: "Change Only the Dog into a Cat"

Once things had taken some shape, I decided on a major change of course: "Actually, I want it to be girls and a cat."

An ordinary illustrator would make a sour face and say, "What, start over from the beginning?" But the deputy manager (AI) didn't complain once.

"Change the characters to two girls, one with long hair and one with short hair. Clothes in yellow and green, in the same hand-drawn style as before."

"Change the dog to a cat, switch the words to the cat-speak you generated earlier, and make poses to match."

"Make the cat a Siamese, not a ginger tabby."

On top of that, I made a request that tested the limits of AI.

"Keep the composition of the 'boys and Shiba Inu' you made earlier exactly as it is, and rewrite only the dog part as a Siamese cat."

To my surprise, the AI understood this complicated instruction. The boys' positions and poses stayed the same, while the people and the animal were neatly replaced with a "Siamese cat."

![The finished illustration sheet for LINE stickers](images/_web/fig-07.jpg)

However, to use them as stickers on LINE, you need to split the illustrations, create thumbnails, compress everything into a ZIP, and upload it.

This too can be done through dialogue with Gemini, but I will explain it again later in 3-6. The First Hurdle: Simple Splitting and the "Image Quality Trap."

### 3-3. Case 2: The "Christmas Banner" Made in 22 Rounds of Dialogue

After the LINE stickers, there is another big piece I made hand in hand with AI. It is the announcement banner for the "Christmas dinner," the biggest event of the year for the shop.

I used an AI called "Nano Banana" (the image generation model built into Google's Gemini).

#### Phase 1: Adjusting Layout and Text

At first, I started by placing the necessary elements (Santa, reindeer, text information) on a wide canvas.

Looking at the images that came out, I gave instructions.

"It feels a bit empty. Add illustrations of a Christmas tree and champagne."

"The menu is a bulleted list and hard to read. Sum it up as 'six courses in all,' and make the title bigger and more eye-catching."

![The image generated at the early stage. Still a bit empty-looking](images/_web/fig-08.jpg)

#### Phase 2: Tuning the "Liveliness"

Once the layout was set, next came the atmosphere. It lacked a "party feel."

I instructed, "Make it livelier! Scatter lots of little Santas and reindeer, balloons, and confetti."

This time, the screen became far too cluttered.

"Sorry, that was too many elements. Reduce the characters once and make it clean."

Being able to repeat this fine-tuning of "adding and subtracting" is AI's strength.

#### Phase 3: The Unexpected Idea of a "Complete Redo"

Partway through production, a doubt crept in. "Wouldn't it look more delicious to show pictures of the food rather than make the characters the main focus?"

So I boldly instructed, "As an alternative, make a design that features illustrations of the actual dishes as the main element."

![Illustration proposal featuring the dishes (some text is garbled)](images/_web/fig-09.jpg)

The AI instantly came up with appetizing food illustration ideas, but after comparing them, I decided to go with the original character design after all. Even a "let's go back to how it was" like this can be asked of AI without hesitation.

#### Phase 4: The Last Line of Defense Is the "Human" Eye

After the final design was decided, I also left the size variations to the AI, for Instagram posts (vertical) and for Stories (even taller).

And then, just as it was about to be finished, I noticed a serious mistake.

"Wait, the day of the week on the date is wrong!"

AI is good at drawing pictures, but it does not understand the days of the week on a calendar. If I had posted it as it was, it would have been a disaster.

I hurriedly instructed, "Fix the date to '12/24 (Wed) and 25 (Thu)'!" and finished the final version.

![The final banner after correction](images/_web/fig-10.jpg)

A total of 22 rounds of revisions and dialogue.

AI is not a magic wand, but if you talk with it patiently, there is no more dependable design partner.

### 3-4. Case 3: A New Year's Opening Notice That Evolves with the Situation

The excitement of Christmas has barely faded when the next event arrives: year-end and New Year's business.

For a restaurant or bar, getting the word out at this time of year is a race against the clock. "Until when are you open at the end of the year?" "When do you reopen in the new year?" Customers are always looking for information.

But information changes by the minute.

"Once year-end service is over, I want to rewrite it so it only shows the New Year's notice."

"I posted it on X (landscape), but I want to run it on Instagram (portrait) too."

If I had asked an outside designer to do this, the revision fees alone would be a nightmare, and above all it wouldn't be done in time.

So once again I teamed up with an image-generation AI (Nano Banana) and got to work on banners to carry me through the year-end and New Year's season.

#### Step 1: The Style Is "80s Crayon Drawing"

First, I built the overall look and feel.

What suits my bar is not glossy CG.

"A warm style like an 80s-era hand-drawn crayon picture, with visible brushstrokes. Keep the background plain white."

With this instruction as the core, and with an announcement on X (formerly Twitter) in mind, I started work on a landscape canvas.

#### Step 2: The Departing Snake and the Arriving Horse. A Toast to Pass the Baton

At first I thought about drawing just one zodiac animal, but this was, after all, the turn of the year.

I had an idea: "I want both the outgoing year's animal (this year's zodiac sign) and the incoming year's animal (next year's) to appear."

So I gave the AI this instruction:

"Put a group of snakes (the Snake year) on the left side of the screen and a group of horses (the Horse year) on the right. Have them each hold a beer mug and cheerfully toast, as if passing the baton at the end of the year."

The image the AI generated was exactly what I had pictured.

Charming snakes on the left, dependable-looking horses on the right, drinking together across the boundary between species.

From "year-end (Snake)" to "New Year (Horse)."

In a single picture, the passage of time and the festive mood were beautifully condensed.

![A generated image of a snake on the left and a horse on the right toasting, expressing the old year giving way to the new](images/_web/fig-11.jpg)

#### Step 3: "Acting Direction" and "Costume Fitting" for the Animals

Once the composition was settled, the next job was the finer staging. Here too, the AI put up with my picky demands.

In the first images, the animals were just standing in a row, or held their mugs in unnatural ways.

"Make them look happier! Like regulars having a great time together."

"I also want a seasonal feel. Put scarves and bow ties on them, give them a winter look."

With that one remark, the animals on screen wrapped themselves in warm-looking red and green scarves and were instantly transformed into the stars of a "winter party."

"Yes, now it has that warm feeling of daytime drinking on a cold day."

Looking closely, some of the hand movements and the way they hold the mugs are still unnatural. But being particular means taking more time. Trading off time against how well the message comes across, I accept a reasonably good result.

#### Step 4: As Time Passes, the Information Changes

From here on is where AI really shows its worth.

The original banner showed both the December and January schedules as the "Year-End and New Year's Business Schedule."

But once December 31 has passed, the year-end information is no longer needed.

I opened the project I had been working on and asked for a major change to the text.

1.  Change the title: from "Year-End and New Year's Hours" to "Daytime Drinking Opens in the New Year."

2.  Tidy up the information: delete the December schedule that was over and narrow it down to just the "New Year's schedule (1/2–1/4)."

3.  Fix the zodiac characters: change the snakes of the outgoing year into horses.

4.  Add a hook: add an attractive offer, "all-you-can-eat-and-drink highballs and fried chicken," as a new draw for customers.

![Step 4: As Time Passes, the Information Changes](images/_web/fig-12.jpg)

Without recreating the image from scratch, I could refresh the information as if rewriting the words on a chalkboard. That is the strength of AI design.

#### Step 5: From X to Instagram. A Format That Changes at Will

And now, the final touch.

"I've announced it on X. Next I want to run it in Instagram Stories."

But Stories use the "portrait" size, which fills the whole phone screen. If you put a landscape image in as it is, you get empty bands above and below, and it looks bad.

With an ordinary illustration, this is the kind of change that would mean redrawing it.

But all I did was tell the AI:

"Keep this design, but rearrange it into a portrait layout for Instagram Stories."

The AI rearranged the animals, who had been spread out sideways, into a vertical arrangement, adjusted the balance of the text, and instantly generated a design tailored for smartphones.

![The finished portrait image for Instagram Stories](images/_web/fig-13.jpg)

### 3-5. Case 4: Making the Bar's Logo - A Dialogue That Turns "Meaning" into "Form"

Beyond "pictures" like banners and stickers, I also took on a more abstract challenge with the AI: designing a new logo.

It's meant to be built into banners and the like, so that people can recognize Tamuro at a glance.

The subject is Tamuro, the referral-only bar I run at night. This name carries a strong wish: "to be a place where all kinds of people gather freely and happily (tamuro-suru, to hang out) in the town of Higashi-Nakano."

How could I condense this invisible "story" into a small logo mark? A patient dialogue with the AI began.

#### Step 1: Choosing the Lettering and the Design Direction

At first I threw ideas at the AI, such as "a sober look with the kanji 屯" and "something poppy in katakana," and had it produce a few rough drafts.

But none of them felt right. Given the nature of the bar, I wanted something more modern, with a neutral feel that welcomes diversity.

So I changed course.

"Let's base it on the highly versatile alphabet, 'TAMURO.' The style should be 'flat design' without complicated decoration. And the color should look strong even as a single color."

The AI immediately proposed a simple, bold sans-serif "TAMURO."

![The sans-serif logo](images/_web/fig-14.jpg)

#### Step 2: Breathing "Meaning" into the Shape

This is where the real test begins. Plain letters mean nothing. And having only the "M" in the center doesn't convey much either.

"I want to express the origin of the name, 'people gathering.' Could you pull the whole thing into a friendly 'circle,' while shaping each letter of the alphabet so it looks like a person moving happily?"

This is a very abstract order. But the imagination of my deputy manager (the AI) exceeded my expectations.

What the AI came up with was a design in which the skeletons of the letters "T," "A," "M" and the rest were transformed into silhouettes of people dancing with their arms and legs stretched out.

![A logo that maps the alphabet onto people](images/_web/fig-15.jpg)

#### Step 3: The Tug of War Between Design and Legibility

"Interesting! But like this, you can't read 'TAMURO'..."

If you put too much weight on design, it stops being recognizable as lettering, and if you put the weight on the lettering, it loses its charm. I ran into this dilemma.

From here, it was a matter of repeated fine-tuning.

"The letter 'A' looks like a person, which is good, but emphasize its structure as an 'A' a bit more. Put the crossbar in firmly."

"The overall balance is good, but the people are packed too tightly and look cramped. Leave a bit more cheerful space."

"Combine the dancing people from before with the TAMURO letters, and make it a circle!"

![The circular "TAMURO" logo mark, completed after trial and error](images/_web/fig-16.png)

Though it is made of lively silhouettes of people, one look at the lower part and you can clearly read "TAMURO."

By tossing ideas back and forth with the AI again and again, I got a logo I was happy with, one that fuses legibility, design quality, and above all the "wish" I put into the bar.

It is now used as the icon for the bar's X (formerly Twitter) and Instagram accounts.

### 3-6. The First Hurdle: Simple Splitting and the "Image Quality Trap"

The creative challenge of making the logo was over.

But the work wasn't done yet.

Back to the LINE stickers. What I had in hand was a "sheet" with 25 illustrations drawn on a single page.

To apply for them as LINE stickers, I had to cut each one out, make the background transparent, and resize it. It was a tedious job I had been putting off.

"There's no way I can cut these out by hand..."

I consulted Gemini and asked for a solution. Gemini said, as if it were nothing:

"Let's automate it using a programming language called Python."

Honestly, I nearly gave up right there.

"Python? I've heard the name, but installing that kind of software on my computer is scary. The setup sounds difficult too. Please don't expect that much from a guy who runs a bar..."

But this is one of the highlights of the book. As if sensing what I was thinking, Gemini made a surprising suggestion.

Gemini:

"You don't need to set up any environment at all. Use a free Google tool called 'Google Colab.' It runs in your browser, so all you have to do is copy and paste the code I write into it."

"What? There's something like that?"

I couldn't believe my ears. I had never imagined there was an environment where programming runs in nothing but a browser, with nothing installed on my own PC.

Not "after I study Python," but "having the AI teach me even the existence of the tool (Colab)."

At that moment, my assumption that "programming means a lot of preparation" collapsed.

### 3-7. Don't "Read" the Error Screen, "Snap and Send" It

As instructed, I opened Google Colab, pasted in the code, and pressed the play button.

But reality isn't that kind. What appeared on the screen was a string of bright red text... an error message.

"Error: Image file not found..."

The old me would have had an allergic reaction just seeing this error and quietly closed the browser.

But now I had an ally: "multimodal" AI, an AI with eyes.

I didn't even try to read the error message.

I just took a screenshot of the screen and pasted it, splat, into Gemini's chat box.

And I added a single line: "Some kind of error came up."

![Pasting the Google Colab error screen into Gemini as it was](images/_web/fig-17.png)

Gemini analyzed the image right away and sent back an answer.

Gemini:

"Ah, the file name of the image being loaded is wrong. I've corrected the code to use '.jpg'. Please run it again with this version."

"...Wow, this is fun!"

This exchange felt less like programming and more like a "spot-the-difference" game or a game of catch.

- Me: (pasting a screenshot) "It stopped again."

- Gemini: "The image size doesn't match. I'll add a function that adjusts it automatically."

- Me: (pasting a screenshot) "This time the image looks rough."

- Gemini: "I forgot to add the process called 'LANCZOS' that preserves image quality. I'll fix it."

I don't understand a single line of the code. When an error appears, I just take a screenshot and throw it to the AI with "Look!"

This "handing off the error analysis" was the biggest secret to how I, with zero knowledge, managed to build a system, and at the same time it was the most exciting experience of all.

### 3-8. The Biggest Wall: "Hand-Drawn Misalignment" and "Overflow"

As I kept up this "conversation called errors," the system became more and more refined.

And at last I entered the biggest challenge: "Phase 2: Automatic Cutting of Hand-Drawn Layouts."

I got greedy.

"Let's make a sheet of 5×5, 25 stickers. And since I want more of a handmade feel, I want to place them freely, without being bound by the grid lines."

With code that simply divides the sheet equally, a character's hand or lettering spills into the next cell and gets cut off miserably.

I also tried a method of "cutting out everything except the white background," but the margins came out uneven and it failed.

I was about to give up. Then, drawing on my instincts from my days as a systems guy, I told Gemini:

"I want you to drop the idea of cutting the image with scissors. Instead, look at which cell the 'center point' of each picture is in. If the center is in that cell, then even if it overflows a bit, treat the whole picture as 'belonging to that cell' and drop it into that cell's bucket."

This was the solution I named the "grid bucket method."

Why did I come up with "putting it in a bucket by center point" instead of "cutting with scissors"?

The amateur's way of thinking (analog): You imagine "snipping a single picture with scissors." That way, you cut right along the line, and the character's hands and feet get chopped off.

The systems guy's way of thinking (digital): A computer has no physical sense of "cutting." Instead, it has "coordinates (positions)." This is how I saw it: "Even if it overflows a bit, as long as the picture's 'belly button (center point)' is inside the cell, we can just consider the whole picture as 'belonging to this cell.'"

![The analog idea of "cutting along lines" and the digital idea of "choosing by point"](images/_web/fig-18.jpg)

This is what it means to "translate vague analog work into clear digital rules." When you give instructions to an AI, thinking up a rule like this, one where the answer comes out the same "no matter who looks (or calculates)," works well.

Gemini turned this abstract request into code beautifully. The result was perfect.

The "Thank you!" lettering and the tails that had spilled into neighboring cells were all recognized cleanly and collected as single stickers.

It even honored my selfish request, "The last one (the 25th) isn't needed, so skip it." At last, I had a tool where "you just drop in the image and press a button, and a complete set of images for the LINE application is produced."

All I did was convey the "problem on the ground (the pictures get cut off)" and propose a "logical solution (decide by the center point)." The AI wrote all the difficult code.

This is the very essence of "vibe coding," building systems starting from zero knowledge.

#### Chapter 3 Summary

1.  AI drawing is not "one and done." You can remake it as many times as you like to suit the situation: changing characters, adding a seasonal feel, switching media.

2.  Even an abstract "concept (people gathering)" can be turned into a "form (a logo)" through repeated dialogue.

3.  Tedious jobs (cutting out images) are exactly what Gemini × Google Colab can automate. Errors can be solved with screenshots.

#### Column 1: A Crash Course in "Google Colab" for the Liberal-Arts Owner

~Use a "rented kitchen" and leave your own PC as it is~

"Google Colab," which appeared in the main text. Doing programming (Python) on your own computer is like "making authentic ramen from scratch, starting with the soup, in your home kitchen." The preparation is a lot of work.

Google Colab, on the other hand, is "a free rental kitchen fully stocked with cooking tools." Just open your browser and the best tools are ready. You don't need to change any settings on your computer. You can program with just a browser while keeping your environment clean. First, search for "Google Colab" and take a peek at this rental kitchen.

#### Column 2: Not "Reading" the Error Screen Is the Right Answer

~Master the ultimate weapon: the screenshot~

When an error appears, are you earnestly trying to decipher the English message? That's a waste of time.

When something tastes off while you're cooking, you ask the chef to taste it. In the same way, just show the AI a "screenshot (screen capture)."

- Windows: \[Win\] + \[Shift\] + \[S\]

- Mac: \[Cmd\] + \[Shift\] + \[4\]\
  Press these, draw a box around the error, and paste it into Gemini. That's all. Don't "read the error," "show the error." Just changing your mindset this way will triple your development speed.

I've introduced several examples so far, and everything I'm doing comes down to the following three points.

・Don't demand the finished form in one go (it's fine to assume a dialogue)\
・Say "no, that's not quite right" without hesitation\
・Assume the cost of revisions is zero and toss requests out casually

You don't need design talent. All you need is the courage to put "something bugs me" into words.

## Chapter 4: Practice Part 2 - Making Daily Work More Efficient (Using Multimodal AI)

~Finish "tedious data entry" with a single smartphone~

### 4-1. The Trouble with Updating the Wine List

For a bar or restaurant owner, updating the menu book is an unglamorous but heavy burden.

What troubled me most was making the "wine list."

Every time a new wine arrives, the following work is needed.

1.  Look at the bottle's label (foreign-language cursive, hard to read).

2.  Type the brand name and vintage (year) into the PC without mistakes.

3.  Look up the wine's characteristics and flavor online.

4.  Write an "introduction" that makes customers want to read it.

5.  Think of dishes that go well with the wine (pairings).

Doing all this with a dictionary in hand, in the gaps between busy service, is nearly impossible. I would put it off with "I'll do it later," and the recommended list often ended up never being updated.

### 4-2. Just Snap a Photo. The Shock of the "Wine List Gem"

So I decided to try Gemini's "multimodal feature (image recognition)."

The method is so simple it's anticlimactic.

1.  Take a photo of the wine bottle with your smartphone.

2.  Send that photo to Gemini.

3.  Add one line: "Make it a list."

That's all.

![A photo of an actual wine bottle label taken with a smartphone](images/_web/fig-19.jpg)

Gemini then instantly reads the label information from the photo.

It not only transcribes the brand name, such as "Cave d'Occi Winery, Tsukimi de Ippai 2024," but also searches a huge online database for its characteristics and automatically generates an appealing description.

What surprised me even more was that it also output "pairing suggestions" as a set.

Suggestions like "The rich aroma of this wine goes well with ○○" appeared on the screen within seconds.

The hours I used to spend wrestling with a dictionary had shrunk to a single click of the phone's shutter.

### 4-3. Making Your Own "Gem"

To make this work dramatically more efficient, I went on to use a feature called "Gems."

It's a "custom AI feature of your own" in which you can have the AI memorize a particular role and rules in advance.

Explaining everything from scratch each time, "You are a sommelier. Look at this photo and..." is a hassle.

So I registered the following "instructions (prompt)" with Gemini in advance. This is the inside of the head of my bar's "dedicated sommelier AI."

#### The Instructions I Actually Have Registered

> Read the image and create a wine list in the following format.
>
> For prices, do not use market prices. Calculate them assuming the bottle price at a typical restaurant (about 2.5 to 3 times cost).
>
> Do not use a table format. Create it so that it fits on one or two sheets of A4 paper.
>
> The format is only a reference; create the list using only what has been input.
>
> The format is below.
>
> United Kingdom 🇬🇧
>
>  Ridgeview Bloomsbury NV  ¥8,500 (about $57)
>
>  Pale gold with pleasing bubbles. Hints of melon and honey among citrus aromas... (the rest omitted)

In fact, the lower half of this prompt, the "format (sample)" part.

I did not come up with it from scratch.

Earlier, when I was searching for wine information online, I would think, "Oh, this shop's description is easy to understand," or "The way this site writes makes it sound delicious," and I had simply copied and pasted such passages into a notepad, over and over.

I threw that "patchwork memo" at Gemini as it was.

"These are passages I copied and collected a while back. Imitate this feel and write about the wine in the new photo too."

That's all I told it.

Even so, this instruction contains three tricks that reduce the burden on the shop floor.

① "The price calculation logic"

This is the biggest time-saver. Because I instruct it to give "the price a restaurant would charge" rather than "the market price," the AI works backward from typical purchase prices and gives me a figure like "¥8,500 (about $57)" that can go straight on the menu. (Of course the final decision is the owner's, but having a guide makes things easier.)

② "Not a table format, but fitting on A4 paper"

If the output comes in a table format like Excel, the layout falls apart when you paste it into the menu book. By having it write in an "A4 menu format" from the start, I aim for output that can be printed and used as it is.

③ Using copy-pasted web text as a "sample"

Instead of vaguely asking, "Write a nice description," I show it a concrete example (my copy-pasted memo): "🇬🇧 flag + wine name + price + sensual description."

When an AI is shown an example, it understands, "Ah, so this is the tone and manner I should write in," and the accuracy of the output jumps. In technical terms this is called "few-shot prompting," but it's essentially the same as "teaching by letting them watch your back."

And that "back" can be perfectly well made of found text, the written equivalent of a found photo from the web.

![The finished wine list text output by Gemini](images/_web/fig-20.png)

### 4-4. It Doesn't Even Have to Be an Image. The Copy-and-Paste Revolution from LINE

What's great about this "Wine List Gem" is that the input isn't limited to photos.

In fact, at a bar you often place orders with the liquor store over LINE, don't you?

When the order is done, a message like this arrives from the liquor store.

> "Thank you as always. We've received your order as follows.
>
> ・Cave d'Occi Tsukimi de Ippai Blanc 24 3 bottles
>
> ・Ridgeview Bloomsbury 6 bottles
>
> ・○○ (new wine) 2 bottles
>
> We'll deliver tomorrow."

One day it suddenly occurred to me: "Couldn't I use this text as it is?"

As a test, I copied this LINE message with my finger and tossed it straight into Gemini.

The result was perfect.

Gemini recognized only the "product names" in the LINE message, searched for information online, and made a list in the usual format (flag + price + description).

In other words, I don't even have to wait for the bottles to arrive and take photos.

At the very moment I place the order, just by copying and pasting inside my phone, the menu list is finished before the products even arrive.

No need to open a PC, no need to start the camera.

In a corner of the kitchen, or on the train, the work is done with nothing but phone operations.

Isn't this the "real efficiency" that a one-person solo owner should get?

### 4-5. The AI's Suggestion × the Judgment of the Shop Floor (Reality)

Still, I don't swallow the AI's suggestions whole. What matters here is our "human judgment on the shop floor."

One time, the AI made this suggestion to go with a wine:

AI: "For this red wine, roast duck with orange sauce is a perfect pairing."

A wonderful suggestion, but unfortunately that day there was no duck in the shop's refrigerator.

I don't think, "The AI says so, so I have to buy duck." Here is how I think:

Me (on the shop floor): "We don't have duck, but today some good free-range chicken came in. It has fat comparable to duck, so I'll sear this chicken until the skin is crisp and finish it with an orange-flavored sauce, just as the AI says."

"The AI's knowledge (duck and orange go together)" × "the shop floor's stock (we have chicken)" = "a new menu item that is decisive and realistic."

This combination is the real pleasure of developing menus with AI.

The AI gives you the textbook answer, but it doesn't know what's in today's refrigerator. Filling in that gap is your job as the owner.

### 4-6. The Last Mile: AI Can't "Taste"

There is one more thing you must never leave to AI.

It is the tasting you do before anything goes out to a customer.

The descriptions and pairings the AI writes are based on "general data from the world at large."

But wine is a living thing. Even the same label changes in flavor with the vintage and how it has been stored.

Once, the AI wrote a description for a white wine: "A fresh, light, dry wine. Perfect with seafood carpaccio."

But when I actually opened the bottle and tasted it, it was more aged than I had expected, with rich, honey-like notes.

"If I serve this as a 'light, dry wine,' the customer will be disappointed... It would go better with chicken in cream sauce than with carpaccio."

I corrected the text Gemini had produced right away.

- Before (AI): "Fresh and light. Good for appetizers"

- After (human): "Rich, full body from aging. Strong enough to stand up to a main course"

The AI makes 90% of the draft, and the human tastes it and adds "the last 10% (the soul)."

This check is the responsibility of a restaurant owner, and it is something AI can never imitate.

Not "because the AI said so," but "because I drank it and it was delicious."

To serve with that confidence, I still taste freshly opened wine today, with a list the AI made in one hand.

#### Column 3: Tips for Photographing Things So the AI Sees Them "Correctly"

~ Like showing a label to a sommelier ~

When you send Gemini a photo, a few small tricks can dramatically improve how well it recognizes what it sees.

1.  Avoid glare: Bottle labels reflect light easily, so change the angle a little, or cast a shadow with your body when you shoot.

2.  Take several shots and send them together: For things like the contents of a refrigerator, send a wide shot and close-ups together, and the AI will recognize even the items in blind spots.

3.  Point with your finger: It also helps to point at the spot you want the AI to look at as you take the photo. Put something like "I am pointing with my finger" in the prompt. It is the same as pointing at a menu in a restaurant abroad.

## Chapter 5: Applications - Business Analysis and Profit Improvement

~ Dig up the "invisible gold mine." A management meeting with your AI consultant ~

### 5-1. The Night I Rack My Brain Over a Calculator at the End of Every Month

For those of us who own small independent restaurants, no time weighs on us like the monthly closing work.

In the late-night quiet, tallying the register data and typing it into Excel, all you hear is your own sigh.

"This month's sales target was ○○0,000 yen. ...I missed it."

"The number of customers isn't bad. We were full on the weekend. But for some reason the spend per customer isn't growing."

Why can't I hit the target? The food should be good. I'm working hard on service.

"Maybe the prices are too high?"

"No, if I go any cheaper I won't make a profit. And ingredient costs are going up, too."

Questions with no answer go around and around in my head, and in the end I wrap it up with pep talk: "Next month I'll put in more spirit and push the recommendations harder." This was my bad habit, and that of many owners.

But now I have an advisor with no emotions.

I faced Gemini with that month's sales data and the data from the shop's menu.

### 5-2. An Experiment: Making the AI Read "Visuals" and "Numbers" at the Same Time

This time, I gave Gemini three pieces of information.

I threw in, all mixed together, the "design (right brain)" and the "numbers (left brain)" that I had always managed separately.

1.  "This month's sales target"

- My earnest wish. The number I absolutely have to hit.

2.  "All the data from recent sales slips (CSV/Excel)"

- The result in reality. The cold facts of who ordered what, and at what price.

3.  "A PDF file of the current menu"

- The world the customers see. Visual information such as photo placement, text size and color.

And then I asked this.

It was not a work order like the earlier "make an image." It was a question, the kind an owner asks.

> "Compare the current sales data (reality) with the layout of the menu (appearance).
>
> Point out the bottleneck: what are we missing to reach the target of ○○0,000 yen?"

### 5-3. The "Owner's Assumption" the AI Saw Through

A few seconds later, Gemini's answer came back, and it struck right at my blind spot.

I had assumed I would get general advice like "Let's develop a new menu item" or "Let's promote on social media."

But what the AI pointed out was a fact I had been unconsciously trying to hide.

Gemini's answer:

> "Cross-checking the data against the menu, I found a major missed opportunity.
>
> The all-you-can-drink plan, which has a high profit margin and can reliably raise the spend per customer, is currently listed on the menu (Before) only in text, quietly, at the very bottom left.
>
> Meanwhile, the best spot on the menu, at the very top, holds the low-priced 'Set ¥2,200 (about $15).' This way, customers drift to the cheaper plan and never even notice the higher-priced all-you-can-drink option."

Looking at the screen, I couldn't help but groan. It was exactly right.

We do have an all-you-can-drink plan. But somewhere in my mind, I had been thinking this:

"We're not a chain izakaya *(a casual Japanese pub that serves food and drinks)*. Selling all-you-can-drink in big letters looks cheap."

"I want people to savor the taste of the wine, so only those who know about it should order it."

That "assumption" of mine showed up in the menu layout, in the text at the very bottom.

![The Before menu. The all-you-can-drink listing is in the lower left and doesn't stand out. It's also hard to tell that food is separate](images/_web/fig-21.png)

The AI did not miss it.

"Owner, you want to hit your target number, right? Then you should put the course you most want to sell, the one with all-you-can-drink, right at the top, proudly."

### 5-4. No Image Material? Then Let the AI Draw That Too

I made up my mind. "If looking cool just makes sales drop, I'll try it, whatever it takes."

But here a problem came up.

"Even if I put it big at the top, text alone is weak..."

And if I grab a photo of people toasting with beer from a free-stock site, it instantly looks like a chain restaurant. It doesn't fit the atmosphere of my shop.

I have no talent for drawing, and hiring an illustrator costs money and time.

I started to worry, "What should I do...?" but then I remembered right away.

"That's right, I have a deputy manager (the AI) who can draw."

I had found something close to the image I wanted on a stock-material site. It said modification was allowed.

I went on to type this into the chat box:

> "Draw an illustration to put at the top of the menu. Use the attached image as the base.
>
> I want the feeling of people happily toasting, but without looking cheap.
>
> Please do it in a simple line-drawing style."

A few seconds later, four illustration candidates appeared on the screen.

From among them, I chose the simple, warm "Cheers!" illustration that best matched the shop's atmosphere.

![The "Cheers!" illustration the AI generated in just 10 seconds](images/_web/fig-22.jpg)

It took only 10 seconds.

Not just the analysis: the "material" needed for the improvement can be procured on the spot.

This is the real strength of building generative AI into your management.

### 5-5. Just Changing the Layout Raised the Spend per Customer by About 40%

So I redesigned the menu.

#### Before: The Menu as It Was

- Best spot (very top): Low-priced items such as "Set ¥2,200 (about $15)" and "Course Set ¥3,300 (about $22)."

- All-you-can-drink: Listed in text only, in the lower left corner, as "All-you-can-drink from ¥3,000 (about $20)." It was completely buried.

#### After: The Revised Menu

- Best spot (very top): High-priced plans of ¥4,500–¥5,700 (about $30–$38), presented as "Our top pick! Full Enjoyment Course (with all-you-can-drink)."

- Design: With the AI-generated "Cheers!" illustration added, it strongly guides the eye, visually, to "Look here first."

- Layout change: The cheap set menus that used to be the stars were moved below.

![The After menu. The all-you-can-drink course is placed at the very top](images/_web/fig-23.png)

The food, the prices and the quality of the drinks are, in fact, almost unchanged. All I changed was "how it is shown" and "where."

And the result?

From the next day, customers' ordering behavior changed dramatically.

The first words from customers opening the menu were no longer "Beer for now," but "Then let's have this 'Top Pick Course (¥4,900 (about $33))' with the illustration."

Customers who used to finish with "the Set (¥2,200 (about $15)) plus two drinks" (a spend of about ¥3,500 (about $23) per customer) now chose the ¥4,900 (about $33) course from the start.

With this alone, the spend per customer jumped by ¥1,400 (about $9.3).

On top of that, customers also gained the benefit of "being able to drink without worrying about the bill," so satisfaction went up rather than down.

### 5-6. Checking the Answers with the December Sales PDF (PDCA)

One month had passed since I put the measure into action.

Not stopping here is the essence of using AI.

Many owners judge results by feel and leave it at that: "We were busy, so it must have worked," or "Sales went up, so that's good."

But I faced Gemini again.

This time I uploaded the "PDF of December's sales data," where the results were in, and asked this:

> "The results of last month's measure (the menu change) are in.
>
> Look at this December sales data and check the answers (evaluate): has the number of 'Top Pick Course' orders gone up as intended, and how did it affect the spend per customer?"

Gemini analyzed the data instantly and sent me back a report.

![Gemini's sales analysis report screen: I made a summary for publication, so the content partly differs from the text below](images/_web/fig-24.png)

Gemini's analysis:

> "These are excellent results. Looking at the trend in the data, the number of 'Full Enjoyment Course' orders rose to about 1.8 times the previous month.
>
> As a result, the overall spend per customer rose by an average of ○○ yen.
>
> The main factor is that placing the all-you-can-drink plan higher raised the order value, especially for groups."

Hearing those words, for the first time I felt truly at ease.

Not "we somehow made money," but the confidence of "I aimed, and I made the numbers."

This becomes the driving force for the next measure.

1.  Plan: Look at the sales data and the menu, and find the problem (the all-you-can-drink plan is hidden).

2.  Do: Have the AI draw an illustration and change the menu layout.

3.  Check: Have it read the December sales PDF and verify the results.

4.  Act: Think about reviewing the food menu layout next.

The "PDCA cycle" that big companies run at enormous cost can be run by an individual owner like me, with just a smartphone, if I have the AI as a partner.

## Chapter 6: Challenges - Developing a System Just for My Own Shop

~ "If it doesn't exist, build it." A system development project with no experts ~

※Just so you know, you don't need to do everything in this book.

・Send an image and have the AI write text\
・Turn a long LINE message into a diagram

These two are enough to start. Even that will definitely make your work easier.\
It is also enough to simply read this as a story and think, "So you can do even this much with AI."

### 6-1. Off-the-Shelf Apps Can't Reach the Spot Where I "Itch"

So far I have talked about using AI on top of existing platforms, such as image generation and menu analysis.

But as you keep running a business, worries come up that "off-the-shelf apps" simply can't solve.

In particular, for an irregular business model like ours, "curry by day, bar by night," the flow of money in and out is complicated too.

"I want to match my PayPay Bank balance against upcoming payments and know the amount I'll land on at month-end."

"Payment dates are split between the 10th and the 25th. I want to simulate that."

The accounting software out there is highly capable, but nothing pinpointed "the worry in my head right now."

So I made up my mind.

"If it doesn't exist, I'll build it. I have Gemini, the strongest engineer."

### 6-2. Phases 1–3: From Scribbled Notes to the "Cloud"

Development began with showing Gemini my notes in Google Keep.

![The Keep note that was the starting point of development](images/_web/fig-25.png)

#### Phase 1: Building the Logic

"I want to automate the calculations in this note."

In response to my request, Gemini quickly put together the calculation logic.

- When I change the amount for an item, it instantly calculates the final balance.

- If funds are about to run short, it shows a "warning" in red.

- It simulates payment timing split into "the 10th" and "the 25th / month-end."

- Data is saved in the browser (cache).

This alone was convenient enough, but I got greedy. "I want the data to stay even when I close the browser. I want to check it on my phone, too."

#### Phase 2: Adopting an Unfamiliar Tool, "Firebase"

I had been thinking of linking to a spreadsheet, but Gemini's suggestion was unexpected.

"If you think about real-time performance and efficiency, let's use Google's 'Firebase.' The free tier is enough to run it."

"Firebase...?" I had never heard the word. But with the instinct of my days as a system coordinator, I decided, "If the AI recommends it this strongly, let's go with it."

As a result, by using a database called Firestore, the data came to be stored safely in the cloud.

#### Phase 3: Google Login and an Approval System

It's about money, so it's bad if anyone can see it.

At first I thought of something like a "password phrase," but Gemini suggested, "If you want stronger security, let's use Google login."

Then, when I said, "I want only the staff I approve to be able to see it," it even built "a system where an administrator can approve and remove members on screen."

### 6-3. Phases 4–5: Taking On the Black Screen (the Terminal)

From here came the biggest hurdle of vibe coding: publishing the app on the internet (deploying).

#### Warning: From Here On, It's the "Black Belt" Course

The next few pages are the most difficult "hands-on" part of this book. You will operate a "black screen (terminal)" like the ones hackers use in movies.

I'll be honest. You will definitely get errors here. I did too. You'll run into walls like a "PowerShell permissions error" that read like spells. But don't be afraid. What you do here is the same: just "take a screenshot of the error screen and throw it to the AI."

The truth I learned in my days in the system business is this: "Even professionals get errors. The only difference is whether you give up when one appears, or search (ask) for help." If it seems too difficult, skip this section and just take away the possibility: "You can do even this much with AI."

Gemini said:

"We'll set up the development environment on your Windows PC. Install 'Node.js,' and type the following commands in 'VS Code.'"

I opened the black screen (terminal) as told, and immediately got an error.

"Cannot run because of PowerShell security restrictions."

An ordinary owner would lose heart here.

But I copied and pasted the error screen and threw it to the AI.

The AI answered instantly: "Lift the restriction with a command called 'Set-ExecutionPolicy.'"

Without understanding what it meant, I typed in the command, then npm run build, firebase deploy...

Each time I typed in those spell-like characters, text ran across the screen and the process moved forward.

And at last, my app appeared on the web.

#### Phase 5: Turning It into a Smartphone App (PWA)

The published app was at first in a "bare-faced" state with a broken design, but this too was solved by adding a setting called "Tailwind CSS."

Then, when I asked, "I want to put an icon on my phone's home screen and use it like an app," it taught me the settings to make it a "PWA (Progressive Web App)."

And so a dedicated app that I made (without writing a single line of code) was born inside my phone.

![The screen of the finished cash flow management app](images/_web/fig-26.png)

### 6-4. Phase 6: The Problem After 30 Days, and the Fix

About a month after I started using it, a problem came up.

"It worked until yesterday, and suddenly I can't access it!"

I panicked and consulted Gemini, and the cause was in an unexpected place.

"The database (Firestore) settings were still in 'test mode (limited to 30 days).' It has expired."

To save the trouble of configuration at the start of development, the AI had deliberately set a rule with an expiration date.

"Let's rewrite the security rules so that 'any logged-in user can keep using it.'"

When I rewrote a few lines of the settings file as the AI instructed, the app came back safely.

This trouble, too, was a good experience for me.

I learned that "a system is a living thing and needs maintenance."

And I gained the reassurance that "even if trouble happens, there is always an answer if I ask the AI."

### 6-5. Case Study 2: The "Face Recognition Project" That Started with a Demo Video on X (Formerly Twitter)

Here is another system development I took on, and the biggest one.

It is "a system that recognizes customers who come in through a camera, and quietly tells me their name, their data and their preferences."

It began with the social media site X, which I was scrolling through casually.

A demo video posted by an engineer came across my feed: using the AI built into Google Chrome (Built-in AI) to explain, in real time, what a webcam was seeing.

My instincts as a former system person kicked in.

"This is 'multimodal.' And if it's built into the browser, couldn't it run entirely on my own PC, without paying for the cloud?"

If this worked, I might be able to build a hospitality system just for my shop, without installing an expensive system.

I copied the URL and threw it to Gemini.

"I want to do the same thing as this. Tell me how to implement it."

#### Phase 1: It Worked, but I Couldn't Tell "Who"

I changed the Chrome settings (flags) as Gemini instructed and pasted in the code, and the same system as the demo ran with no trouble.

When I appeared on the camera, the screen displayed this:

"A man wearing glasses is sitting in front of a PC."

It uses an AI built into the browser called GeminiNano. Its advantage is that it works entirely inside the browser without connecting to the cloud, but it can recognize only general things like "glasses" and "man." It can't go as far as determining who the person is.

It's amazing technology. But as a restaurant owner, I was disappointed right away.

"This won't do."

What I want to know is not a general feature like "a man with glasses," but identification of the individual: "Is this Mr. A or Mr. B?"

#### Phase 2: The Wall of Google Photos Integration, and the AI's Answer

So I put a naive idea to Gemini.

"Connect this system to my Google Photos. It has face-grouping data for my friends and regulars, so if you match against that, you can get the names, right?"

Gemini's answer was cold, but correct.

"I'm sorry, but that is not possible. The face recognition data in Google Photos is highly sensitive privacy information, and for security reasons it is not permitted to be used by outside programs."

Fair enough. The road seemed to end here.

But from here came the real essence of "vibe coding (development through dialogue)." The AI did not just refuse.

#### Phase 3: An Alternative and a Pivot

Gemini went on to suggest this:

"We can't use Google Photos, but it is possible to build your own face recognition system in a local environment using open-source libraries (such as OpenCV or face_recognition). Shall we try?"

I answered "Yes" immediately.

From here, the development plan changed completely. Instead of using Chrome's features, I would build a face recognition system from scratch using a programming language called Python.

#### Phase 4: Wrestling with the Black Screen and Connecting to a Spreadsheet

What I had to do didn't change. I asked Gemini "how to install the necessary libraries" and pasted the answer into the black screen (the command prompt).

When an error appeared, I threw the red text back at Gemini as it was.

A few hours later, the system was finally complete.

1.  The webcam captures my face.

2.  It matches against the "face photo data" in a folder on the PC.

3.  When it finds a match, it looks up the customer list in a Google Spreadsheet.

4.  The screen displays "Mr. Bonta: remaining square bottle ○○ g."

![The face recognition system running. It recognizes the owner's face and displays information. The captured image has been mosaicked using Gemini](images/_web/fig-27.jpg)

Outsourcing cost: ¥0 (about $0.00). My own coding work: zero.

It was the moment a one-of-a-kind "face recognition CRM system" was born in a corner of Higashi-Nakano.

#### Phase 5: And Then I Realize the "Responsibility to Protect"

The system was complete. But along with the joy, I felt a chill run down my spine.

"Wait a moment. Right now, this computer holds customers' face data (biometric information), doesn't it...?"

Until then I had thought, "As long as it works, it's fine." But once it's in real operation, that's a different story.

What if this computer gets infected with a virus? The customers' face data and their preference information (personal information) might leak together.

A standalone PC not connected to the internet would be safe, but as long as I handle reservations and social media, an internet connection is essential.

"Being able to build a useful tool" and "being able to manage it safely" are separate matters.

It was here that I first truly felt the importance of the "cyber risk insurance" that an insurance agent had talked about when they came to pitch to me before.

I had laughed, "A small shop like ours won't get cyber attacks," but now that AI lets us build advanced systems, we individual owners also take on the responsibility of being proper "data managers."

With AI, you can get magical tools.

But I learned that carrying the "staff (literacy)" and the "shield (security measures)" to use that magic is also part of an owner's job from now on.

### 6-6. The "Responsibility" and "Insurance" That Come with Freedom

#### Important: Privacy and Personal Information

This "face recognition system" is an experimental prototype I built to test what is technically possible. If you were to use it in a real shop, your customers' face data would count as "personal information (biometric data)," and it would have to be strictly protected under the law (the Act on the Protection of Personal Information).

If you are thinking of adopting something like this, please keep these two points without fail.

Notify customers and get their consent: You need a process, such as putting up a sign at the entrance saying "We use AI face recognition" and getting consent when customers sign up as members. Secret filming is absolutely not allowed.

Protect the data: You need measures that bring the risk of a leak down to zero, such as managing the data in an environment cut off from the internet.

Being able to build something is not the same as being allowed to do it. If you are an owner with technical skills, please remember that the responsibility for using that technology comes with it.

So far I have been talking about how wonderful a handmade system can be. But as a business owner, I have to tell you about a harsh reality as well.

It is this: "Everything you build yourself is your own responsibility."

With a monthly subscription service (SaaS), if the server goes down, the company apologizes and gets it running again.

But a system built with vibe coding has no "customer support."

If your app suddenly stops working at the lunchtime peak, nobody will come to help.

When Google changes a specification, code that worked fine yesterday throwing errors today is an everyday event.

That is why I make two preparations.

One is an "analog backup."

"If face recognition stops, look at the paper customer ledger." "If the register app goes down, use a calculator and handwritten slips."

Digital tools are only "convenient tools." You must not depend on them so much that when they stop, your shop stops too.

The other is the "insurance" I mentioned earlier.

Cyber liability insurance covers not only the risk of an information leak, but also compensation for lost business when your own mistake stops the system. For an individual owner arming themselves with IT, it is part of being a responsible adult.

"Things will sometimes stop. I will sometimes make mistakes."

Take that as a given, accept the risk, and take measures against it.

Only when we have this resolve can we truly use a "free system" that answers to no one.

### 6-7. You Don't Need an Expert. You Need Persistence

I did not pay a single yen in outsourcing fees for the development of these two systems.

All I used was an AI subscription of a few thousand yen per month, and the persistence of an owner who thought, "I absolutely have to get rid of this worry (about cash flow)" and "I want to make my customers happy."

It is not a matter of "I can't, because I can't program."

If you have something you want to build (the Want), AI will teach you how to build it (the How).

Even when words you don't understand come up (Node.js, PowerShell, Firestore...), there is nothing to fear.

We have the strongest partner there is, "Gemini," to translate them and guide us.

#### Column 4: What's the Difference Between Excel and a Database (Firestore)?

~ Is it a "memo for you to read," or a "ledger for the system to read"? ~

Firebase (Firestore) appeared in the development of the cash flow app. You may have wondered, why not Excel?

A spreadsheet (Excel) is a "notebook that people look at and type into." It is very flexible, but for a system, it is vague about "what is where."

A database (Firestore), on the other hand, is a "neatly organized locker made for the system." Because it is fixed that "the date goes in slot 1 and the amount in slot 2," a program can handle it instantly. It also won't break when several people access it at the same time.

"If you are building an app, use a database, not Excel." Just knowing this will raise the level of your instructions to the AI.

## Afterword: A "Recipe for the Future" Only Your Shop Has

~ AI is not a difficult technology. It is a new partner for "conversation" ~

Thank you for reading this book to the end.

If you try only one thing from this book, try this: "Paste that annoying LINE message straight into the AI and ask it to 'turn it into a diagram.'"

I am not a special AI expert. I have simply repeated, every day, the practice of "talking to AI in the words of the workplace," \
in the battlefield of a restaurant.

That is why I think it is enough if you take home from this book not a "collection of right answers," but only a "way of thinking."

When you opened the first page, what image did you have of the words "using AI"?

"Sounds difficult." "You need programming knowledge, right?" "It has nothing to do with a small shop like mine."

You may have thought something like that.

But now that you have read this record of my "trial and error" this far, perhaps that image has changed a little.

What I did was not make full use of advanced IT technology.

I grumbled, "I can't do this by hand." I complained, "This is hard to use." And I was selfish, saying, "I want it to work more like this."

These days, in the world of engineers, the term "vibe coding" is a trend.

It is a method of building a system by feel, while talking with AI.

Just as a shogi player talks with AI to read the next moves, we too can talk with AI and build the "future of our shops."

Like telling your kitchen staff, "Add a little more salt."

Like asking the fishmonger at the market, "Got any good fish today?"

Speaking to AI and saying, "Make this job easier." That is where everything begins.

I once worked in a company's systems department, coordinating between the "front line" and the "developers."

Now I am doing the same thing between "my own shop" and "AI."

And I am convinced of this:

"An owner who knows the troubles of the front line can become the strongest AI commander."

Start today, you too.

First, take out your phone and talk to Gemini.

"Hey, where should I start with today's prep?"

"How can I make this menu item sell better?"

"This paperwork is a pain. Can you do something about it?"

Don't worry if an error appears. It is a sign that the "conversation" has begun.

Just take a screenshot and send it back with "something looks off."

At the end of piling up those conversations, there waits "time" and "breathing room" you could never have imagined, and "a future that belongs only to your shop."

Now, let's hire a reliable "deputy manager" for your shop too.

Because the recipe for the future will be born from the conversation between you and AI.

### The Three Exits of This Book

This book is free to read as a PDF, on note, and on Google Play. (Only on Kindle, the store's rules require a minimum price.) In return, I have prepared three places you can go after you finish reading. If you use even one of them, writing this book will have been worth it.

1. Try it in your own shop. The Agenda series can be started with a free notebook. <https://bontallc.com/agenda?via=b1-en-gp>
2. Follow what I do. I write about the tools I build next, and about daily life at the bar, on note and X. note <https://note.com/bontallc> / X <https://x.com/tamuro_hnakano>
3. If you are ever in Tokyo, visit Tamuro. One minute from the east exit of Higashi-Nakano Station. You can walk in without a reservation. When this book was first written, Tamuro was referral-only. Today anyone is welcome to walk in, no reservation needed. Reservation site <https://tamuroreservation.vercel.app/?src=b1-en-gp>

To those who came because of this book: when you make a reservation, please enter the coupon code "BOOK." We will serve you one drink on your first visit. If you came without a reservation, just say "I saw the book" when you place your first order. We will serve you the same drink. It is a small device so that I can count how many people came because of the book.

### About the Author

Raku Bonta

A solo owner who runs a restaurant with 11 counter seats and 8 tatami-room seats in Higashi-Nakano, Tokyo.

By day it is a hamburger curry shop fragrant with spice. By night it is a referral-only dining bar serving a daily-changing set meal.

▼ Quatre Epice Hamburger Curry

<https://www.instagram.com/quatre.epice.hamburg.curry/>

![Quatre Epice Hamburger Curry](images/_web/fig-28.png)

▼ Referral-only bar "Tamuro"

<https://www.instagram.com/tamuro.higashinakano/>

![Referral-only bar "Tamuro"](images/_web/fig-29.png)

The shop also puts energy into building community through food, with biweekly wine events, a monthly cooking class, and multi-course dinners.

Before opening the shop on their own 12 years ago, the author worked at a company in "system planning" and "solution architecture."

The titles sound difficult, but the real job was "a coordinator who accurately conveys the front line's wishes of 'we want to do this' to IT vendors and gets them built." Not an engineer doing advanced programming, the author has a career as a "translator" connecting people and technology.

Today, drawing on that experience, the author uses generative AI such as Google Gemini to run their own shop, practicing and sharing "business reform that works even with zero specialist knowledge."

## Colophon

- Title: The AI Deputy Manager
- Subtitle: Just talk to it, and it gets things done. More than I expected.
- Author: Raku Bonta
- Publisher: Bonta LLC
- Edition: English edition, first edition (translated from the Japanese original)
- Published: 2026-10-30
- Language: English
- Translation: translated from the Japanese by AI and reviewed by AI. Short notes on Japanese places, systems and customs were added by the translator. Yen amounts are followed by approximate US dollar figures at ¥150 to the dollar (as of 2026-10-29).
- Free to share

The Agenda series: <https://bontallc.com/agenda?via=b1-en-gp>

Tamuro's Instagram: <https://www.instagram.com/tamuro.higashinakano/>

Tamuro's reservation site: <https://tamuroreservation.vercel.app/?src=b1-en-gp>

note: <https://note.com/bontallc>

X: <https://x.com/tamuro_hnakano>
