## Introduction

This book is a record as of January 2026. Some of the ways I run the shop, and some of the names and specifications of the AI tools, have changed since then. The sequel, 『うちの店は、うちの仕様で』, picks up the story.

### Why a Former Systems Guy Is Talking to AI in a Basement Restaurant

Thank you for picking up this book.

*One Person Runs the Shop, and AI Showed Up Beside Me.*

When you see that title, some of you may think, "That's exactly me." Others may wonder, "What does it mean for AI to show up beside you?"

This is not a technical book about difficult programming. It is a book for people like you, restaurant owners who stand in the kitchen every day, do the prep, and are always busy with customers.

Let me tell you a little about myself.

I now run a small restaurant in the basement of a building in Higashi-Nakano ⟦a residential neighborhood in western Tokyo, just west of Shinjuku⟧, Tokyo.

It has two faces. By day, it is a specialty shop for hamburger curry fragrant with spices. By night, it is a referral-only dining bar serving a daily set meal and drinks.

▼ Quatre Epice Hamburger Curry (Instagram)

https://www.instagram.com/quatre.epice.hamburg.curry/

![Quatre Epice Hamburger Curry (Instagram)](images/fig-01.png)

▼ Referral-only bar "Tamuro" (Instagram)

https://www.instagram.com/tamuro.higashinakano/

![Referral-only bar "Tamuro" (Instagram)](images/fig-02.png)

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

Many of us owners use LINE ⟦Japan's most widely used messaging app⟧ to contact staff.\
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

![The long LINE message I actually sent to the staff, typos included](images/fig-03.jpg)

Even when they see this, busy kitchen staff will skim it with "So basically I just take photos, right?" and miss the specifications for "angle" and "container orientation."

But I have no time to open PowerPoint, line up shapes, and make an instruction sheet.

So I fed this text as it was into AI (an AI tool such as Manus, or Gemini) and asked:

"Summarize the content of this text on one slide, as a 'work instruction sheet' that staff can understand at a glance."

### 2-2. AI Is an "Excellent Translator"

After a few seconds of waiting, what the AI produced was a surprisingly easy-to-understand "diagram slide."

![The "Data Collection and Photography Work Instructions" slide automatically generated by AI](images/fig-04.jpg) ⟦The screen is in Japanese.⟧

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

Sota Fujii, the shogi Meijin (title holder), named "vibe coding" as something he got into this year, in 2025. Even someone from the shogi world, which seems completely unrelated to building systems, reportedly tells AI what they want in Japanese and builds handy tools.

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

But pressing [Windows] + [Shift] + [S] dozens of times a day, selecting an area with the mouse, going back to the Gemini screen, and pressing [Ctrl] + [V]...

Honestly, it tires your fingers, doesn't it?

So what I introduced was a "6-button sub-keyboard."

It is a small, Chinese-made keyboard that costs a few hundred to about a thousand yen, which comes up when you search for "programmable keyboard" on Amazon or similar sites.

![A photo of the 6-button sub-keyboard I use](images/fig-05.jpg)

I have assigned the following shortcuts to these six buttons.

1.  Launch screenshot

2.  Select all (Ctrl + A)

3.  Copy (Ctrl + C)

4.  Paste (Ctrl + V)

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

![Illustrations generated for LINE stickers](images/fig-06.png)

### 3-2. The Bold Request: "Change Only the Dog into a Cat"

Once things had taken some shape, I decided on a major change of course: "Actually, I want it to be girls and a cat."

An ordinary illustrator would make a sour face and say, "What, start over from the beginning?" But the deputy manager (AI) didn't complain once.

"Change the characters to two girls, one with long hair and one with short hair. Clothes in yellow and green, in the same hand-drawn style as before."

"Change the dog to a cat, switch the words to the cat-speak you generated earlier, and make poses to match."

"Make the cat a Siamese, not a ginger tabby."

On top of that, I made a request that tested the limits of AI.

"Keep the composition of the 'boys and Shiba Inu' you made earlier exactly as it is, and rewrite only the dog part as a Siamese cat."

To my surprise, the AI understood this complicated instruction. The boys' positions and poses stayed the same, while the people and the animal were neatly replaced with a "Siamese cat."

![The finished illustration sheet for LINE stickers](images/fig-07.png)

However, to use them as stickers on LINE, you need to split the illustrations, create thumbnails, compress everything into a ZIP, and upload it.

This too can be done through dialogue with Gemini, but I will explain it again later in 3-6. The First Hurdle: Simple Splitting and the "Image Quality Trap."

### 3-3. Case 2: The "Christmas Banner" Made in 22 Rounds of Dialogue

After the LINE stickers, there is another big piece I made hand in hand with AI. It is the announcement banner for the "Christmas dinner," the biggest event of the year for the shop.

I used an AI called "NanoBanana" (※ the name of the image-generation AI tool I use, available in Gemini).

#### Phase 1: Adjusting Layout and Text

At first, I started by placing the necessary elements (Santa, reindeer, text information) on a wide canvas.

Looking at the images that came out, I gave instructions.

"It feels a bit empty. Add illustrations of a Christmas tree and champagne."

"The menu is a bulleted list and hard to read. Sum it up as 'six courses in all,' and make the title bigger and more eye-catching."

![The image generated at the early stage. Still a bit empty-looking](images/fig-08.png)

#### Phase 2: Tuning the "Liveliness"

Once the layout was set, next came the atmosphere. It lacked a "party feel."

I instructed, "Make it livelier! Scatter lots of little Santas and reindeer, balloons, and confetti."

This time, the screen became far too cluttered.

"Sorry, that was too many elements. Reduce the characters once and make it clean."

Being able to repeat this fine-tuning of "adding and subtracting" is AI's strength.

#### Phase 3: The Unexpected Idea of a "Complete Redo"

Partway through production, a doubt crept in. "Wouldn't it look more delicious to show pictures of the food rather than make the characters the main focus?"

So I boldly instructed, "As an alternative, make a design that features illustrations of the actual dishes as the main element."

![Illustration proposal featuring the dishes (some text is garbled)](images/fig-09.png)

The AI instantly came up with appetizing food illustration ideas, but after comparing them, I decided to go with the original character design after all. Even a "let's go back to how it was" like this can be asked of AI without hesitation.

#### Phase 4: The Last Line of Defense Is the "Human" Eye

After the final design was decided, I also left the size variations to the AI, for Instagram posts (vertical) and for Stories (even taller).

And then, just as it was about to be finished, I noticed a serious mistake.

"Wait, the day of the week on the date is wrong!"

AI is good at drawing pictures, but it does not understand the days of the week on a calendar. If I had posted it as it was, it would have been a disaster.

I hurriedly instructed, "Fix the date to '12/24 (Wed) and 25 (Thu)'!" and finished the final version.

![The final banner after correction](images/fig-10.png)

A total of 22 rounds of revisions and dialogue.

AI is not a magic wand, but if you talk with it patiently, there is no more dependable design partner.