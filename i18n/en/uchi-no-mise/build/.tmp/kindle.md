## Introduction

This book is a plain record of how the owner of a 19-seat bar in Higashi-Nakano *(a residential neighborhood in western Tokyo, just west of Shinjuku)*, Tokyo, runs the shop with the help of AI.

The bar is called "Tamuro." The name means a place where people gather. It opened in November 2018, a small place with 11 counter seats and 8 tatami-room seats. In the daytime, in the same space, a staff member runs a hamburger-curry restaurant called "Quatre Épices."

In my previous book, *The AI Deputy Manager*, I wrote about generative AI itself. In the year or so since, AI has changed from a tool that answers questions into a tool that gets work done for you. Give it an instruction, and it writes the program, tests it, fixes its mistakes and finishes the job. We call this kind of AI agentic AI.

Using agentic AI, I built Tamuro's reservation system myself. I built a discount system to go with a price increase. I built a system for nurturing regulars. I built an AI that answers customers' questions. And in the end, I got to the point where a customer can ask Tamuro a question from their own AI and go on to make a reservation.

I also took the handy tools I had made for my own shop, shaped them so other shops could use them too, and began offering them for a few hundred yen a month. That is the Agenda series.

This book describes what I built along the way, what I failed at, and what I had to learn again. It is not only the success stories. I kept building things that worked, going on instinct, and contradictions piled up. I found out later that customers' personal information could be read from outside. The AI wrote facts that the shop had never stated. I have included those failures as they happened.

### How to Read This Book

This book has five chapters.

| Chapter | Content | Best for |
| --- | --- | --- |
| Chapter 1 | A Shop That AI Books (the business side of the reservation system) | Everyone |
| Chapter 2 | Behind the Reservation System (technical) | Builders and anyone curious about technology |
| Chapter 3 | Giving Our Shop's Tools to Other Shops (the business side of the Agenda series) | Everyone |
| Chapter 4 | A System for Building Products Alone (technical) | Builders and anyone curious about technology |
| Chapter 5 | The Future of Small Shops | Everyone |

Chapters 2 and 4 are technical and use more specialized terms. Each opens with a three-line summary of the key points, so if technology doesn't interest you, read just those and move on to the next chapter. Read Chapters 1, 3 and 5 in order, and the story still hangs together as one line.

Wherever I could, I added a plain-language explanation next to each technical term. Even if you have never written a program, I hope you will get a feel for what it means to run a shop with AI.

### About the Author

I worked in IT for about 16 years, mostly in system planning and as the coordinator between the people on site and the development vendors, and then entered the food and drink business. So this is not a story of someone who had never written a line of code building everything with AI alone. I want to be honest about that.

Even so, I can now build and run, on my own while working the floor, something of a scale that once required a team and funding. A few years ago, that would have been unthinkable. I want to describe the reality of that change as concretely as I can.

### How This Book Was Made

I made this book with AI too. Starting from the records I have kept during my daily development work, the AI wrote the drafts, and I read, revised and made the decisions. I also had the AI take the screenshots used as illustrations.

I have read through everything, but text written by AI can have things mixed in that are not true. As I say in the main text, AI says "it's done," and checking that is a human's job. There may be mistakes in this book that I overlooked.

Also, the specifications of AI tools and services change within a few months. The steps, prices and each company's support status described in this book are as of October 2026. When you try things yourself, please check the official information at that time.

If you spot a mistake, I would be glad if you told me on note or X. I will correct things as I learn of them.

### The Three Exits of This Book

This book is free to read as a PDF, on note, and on Google Play. (Only on Kindle, the store's rules require a minimum price.) In return, I have prepared three places you can go after you finish reading. If even one of them is useful to you, writing this book was worth it.

1. Try it in your own shop. You can start the Agenda series with the free notebook. <https://bontallc.com/agenda?via=b2-en-kindle>
2. Follow what I do. I write about the next tools I build, and about daily life at the shop, on note and X. note <https://note.com/bontallc> / X <https://x.com/tamuro_hnakano>
3. If you are ever in Tokyo, visit Tamuro. One minute from the east exit of Higashi-Nakano Station. You can come in without a reservation. Reservation site <https://tamuroreservation.vercel.app/?src=b2-en-kindle>

## Chapter 1: A Shop That AI Books

### 1-1 "Is Anywhere Open Tonight?" You Ask the AI

On a Friday evening, someone who has just finished work talks to their smartphone.

"Is there a place in Higashi-Nakano where I can drink alone tonight? Somewhere not too noisy."

The one answering is not a friend. It is the AI that person uses every day. The AI lists candidate shops, describes the atmosphere of each, and tells them tonight's open times and prices. If something catches their eye, they can go straight to the reservation screen.

This is not a story about the future.

On August 10, 2026, OpenAI added a restaurant reservation feature to ChatGPT. According to the official release notes, it connects with the reservation services OpenTable, Resy and Yelp, and available reservation times appear directly inside ChatGPT's answers. You can also answer questions to narrow down the options, and once you pick a time that suits you, you can go straight on to book. It covers OpenTable worldwide, Resy in the US, and Yelp in the US and Canada.

In other words, the entrance people use to find a place to eat is starting to move from search engines and restaurant review sites to "my own AI."

But there is a condition. The only shops you can book through ChatGPT are those registered with the big reservation services. Small shops that are not listed there are invisible to the AI.

So what should a 19-seat bar in Higashi-Nakano that doesn't use the big reservation services do?

Tamuro chose a different path. Without going through the big services, it connected its own reservation system directly to AI.

When a customer asks their own ChatGPT or Claude, "Is Tamuro open tonight?", the AI queries Tamuro's reservation system directly, checks the open times and prices, and answers. Once the conditions are settled, it points the customer to Tamuro's reservation page with the party size and date and time already filled in. The customer presses the final confirm button themselves.

This "connection point between AI and a shop's system" is called an MCP server. MCP stands for Model Context Protocol, a common set of agreements that lets AI use outside tools and data. I explain the details in Chapter 2.

The big reservation services, in fact, also hand customers over to their own screens at the end. For reservations that need a credit card, the process is completed on OpenTable's screen, and changes or cancellations after booking are handled on each service's side. The AI is the entrance, and the reservation service's screen is where it's confirmed. What Tamuro does has the same structure. The only difference is that no big company sits in between.

And the one who built this system was not an outside development company. It was me, the owner. I gave instructions to the AI, had the AI write the programs, and had the AI run the tests.

Of course, I did not arrive here at the start. It began with a very simple reservation form. Then came a price increase, then ideas for discounts, then a system for nurturing regulars, then failures and rebuilding.

Let me first describe what kind of place Tamuro is, in five lines. One minute on foot from the east exit of Higashi-Nakano Station. 19 seats, 11 at the counter and 8 in the tatami room. About half the customers come alone, and the counter makes it easy to start talking with the person next to you. The food is a combination of four appetizers and one main, and the most popular dish is a sweet, garlicky tonteki (pork steak). The wines are mainly from Spain and Italy, and there are about 20 kinds of Japanese craft gin. You can come in without a reservation.

Let me also state one thing I was aiming for. I didn't want to merely take reservations. I wanted even a small shop to be able to build, by its own hand, the whole flow of getting known, getting people to visit, and getting them to come back. The discounts, the emails and the chat window that appear in this chapter are all parts serving that one purpose.

In this chapter, I rewind time and trace how Tamuro's reservation system grew.

![Figure 1-1: The screen after connecting from ChatGPT to Tamuro's MCP server (October 10, 2026). It reads the shop's information and answers that it can handle open times, courses, prices and guiding to the reservation page *(The screen is in Japanese.)*](images/fig1-1_chatgpt-mcp.png)

### 1-2 The Starting Point: Just Taking Reservations

[Tamuro's reservation site](https://tamuroreservation.vercel.app/?src=b2-en-kindle) was very simple at first. Choose a date, time and party size, enter a name and contact details, and send. A notification reaches the shop. That's all.

I built the first foundation with Google's AI development tool (Antigravity). I told the AI about each feature I thought of, and when something worked, I moved on to the next. It's what is called vibe coding (telling the AI whatever comes to mind and having it build by feel).

For me at the time, it was one surprise after another. Describe the layout of a screen in words, and it takes shape in minutes. Say you want a calendar, and a calendar appears. In the gaps while running the shop, one reservation site came together.

Tamuro is a place you can enter without a reservation. In fact, most reservations are made the same day, and many customers just walk in. Even so, I built a reservation system because I wanted a way to connect with customers before they visit. Once someone reserves, their name and contact details remain. Once their contact details remain, I can invite them to come again.

A reservation system is not just a front desk. It becomes the entrance to a relationship with the customer. This idea led later to the discount system and the system for nurturing regulars.

But for a foundation built on instinct, I ended up paying a big price later. I will write about that in Chapter 2.

### 1-3 Building a Price Increase and Discounts at the Same Time

For a restaurant or bar, a price increase is a decision you can't avoid. Ingredients, utilities and labor all keep getting more expensive. Tamuro raised prices too. I raised each course by about ¥400–¥500 (about $2.7–$3.3).

The increase was large, so it was obvious that if I put it out as it was, regulars would drift away. So at the same time as the price increase, I decided to build a discount system into the reservation system. It doesn't just make things cheaper. It rewards, with discounts, the customers who act in ways that are good for the shop.

The first is the group discount. The more people in the party, the lower the price per person. About half of Tamuro's customers come alone, but if they come in groups, the shop's sales grow a great deal. Even after subtracting the discount, the shop comes out ahead. For customers, too, it is a reason to invite friends. In fact, the number of customers coming in groups using the reservation site's party-size discount has grown.

The second is the early-bird discount. Reserve up to one week ahead and you get 2% off; up to two weeks ahead, 4% off. Most Tamuro reservations are made the same day, so I can't read what's coming. The early-bird discount is a mechanism for locking in future sales. On rainy days and cold days, if reservations are already in, the shop can prepare with peace of mind.

Third, I also built a group-buying mechanism. If a set number of people gathered at a set date and time, a set-meal course would be offered at a discounted price. It was supposed to be a mechanism with the Tamuro spirit, where strangers gather at the same time.

But the group-buying plan was not used at all. Zero results. In August 2026 I stopped this plan and decided not to use it again.

Throwing away something you made feels wasteful. But if you build with AI, the cost and time of building are small. Build small, try it, and if it doesn't work, throw it away. I believe this speed is the greatest advantage of running a shop with AI.

There is one more trick in the pricing. Among the plans, I deliberately place an expensive premium plan. It's fine if almost nobody chooses the premium plan. With a pricey plan beside it, the standard looks affordable. It plays the role of what is called an anchor (a reference point for comparison).

![Figure 1-7: The more people, the lower the price per person (comparison of 1, 4 and 6 guests)](images/fig1-7b_compare.png)

### 1-4 A System for Nurturing Regulars

Once names and contact details remain in the reservation system, the next thing you want to do is nurture the relationship with customers. A system that manages customer information and deepens relationships is called CRM (customer relationship management). Little by little, I added CRM features to Tamuro's reservation system.

When customers register as members, they can see their reservation history on a My Page. If they register a birthday, a birthday perk arrives. Members who haven't visited for a while receive a message calling them back. There is also a stamp card. Three visits earn one drink, five earn a steak and other perks, and after reaching five the count starts over. There is also a feature for referring friends.

I designed the mechanism for inviting a second visit with particular care. In restaurants and bars, it's said that whether a first-time customer comes a second time decides whether they become a regular. At Tamuro, I send two guidance emails, seven days and 21 days after the first visit. The first has no coupon; only the second has one. Rather than luring people with a discount from the start, I first help them remember. If they still don't come, I give them a nudge.

I also took care that emails wouldn't pile up. Customers get at most one message a day. When they overlap, priority goes in this order: birthday, second-visit invitation, call-back to lapsed members, other notices. Members who already have their next reservation don't receive emails inviting them to visit.

Consent to receive emails is off by default. Leaving it on would increase the number of recipients, but a design in which people consent without knowing it could be a problem under consumer protection law. Earn trust rather than numbers. That was my judgment.

There is another small touch in the emails. One "Today's Topic" goes into the reservation confirmation email. Something about the season, wine or food. The AI automatically writes a short topic each day.

The aim is to hand the customer one seed of conversation before they visit. Tamuro is a shop with a lot of conversation among customers. A topic read in the email becomes the first thing they say to the person next to them at the counter. So I didn't let the confirmation email end at "Your reservation has been received," and instead made it deliver a little of the shop's atmosphere ahead of time.

I have swapped out the AI that writes the topics once. I changed it to one that produces topics that are more natural and closer to the shop's tone. However, this is not a mechanism for increasing customers. It is a mechanism for making the experience of those who come a little better. I will write about that distinction again in the second half of this chapter.

Among these mechanisms, the one where results gradually became visible is the "Nice to Meet You" and "Welcome Back" plans. These are easy-to-enter, reasonably priced plans that only first-time customers and customers who haven't visited in over a year can choose. They give both new customers and customers who are drifting away a reason to come.

On the other hand, there was a problem too. Many customers book as guests without registering as members. If I demanded member registration at every reservation, they might give up on booking altogether. So after a reservation is finished, I show a prompt, "Would you like to link this reservation to a member account?", and built a way to become a member afterwards. It raises no hurdle to booking, and ties the relationship together later.

![Figure 1-8: Plans that only first-timers and people who haven't visited in over a year can choose *(The screen is in Japanese.)*](images/fig1-8_welcome-plans.png)

![Figure 1-9: The stamp card on My Page (synthetic data) *(The screen is in Japanese.)*](images/fig1-9_stamp-card.png)

![Figure 1-5: Reservation confirmation email. One "Today's Topic" is included (synthetic data) *(The screen is in Japanese.)*](images/fig1-5_confirm-mail.png)

### 1-5 By the Numbers: About 88% of Reservations Are Same-Day

As I kept adding mechanisms, I noticed something. I couldn't tell which of them were working.

So I counted the reservation data. Of the 244 reservations in the most recent 90 days, 215 were same-day reservations. That is 88.1%. The average is 2.71 reservations per day.

Tamuro was not a place people reserve for, but a place people come to on impulse. It only became clear once I put it into numbers.

Two things became visible from these numbers.

One is how to build the reservation form. If most reservations are for the same day, it is more convenient if the nearest open slot today is already selected when the reservation screen opens. On the other hand, some people who want to book a later date will carelessly send it as today. So I made today stand out on the calendar, and on the confirmation screen I show the date and time large with "Today." I kept the convenience of choosing the same day, and made mistakes easy to notice.

The other is the meaning of the early-bird discount. Many same-day reservations means we can't read future sales. Bad weather alone is enough to lower foot traffic. To increase advance reservations even a little, more people need to use the early-bird discount. This awareness later led to the story of building an AI that posts on the owner's behalf.

To look at numbers, you need a system for counting. The reservation site had no access analytics at all. I couldn't tell how many people came to the reservation page, how many quit partway, and how many finished. So I added a system that counts three stages: arrived at the page, decided on the details, finished the reservation. It doesn't record who came, only the stage and the time.

Later still, I also built a system that emails a weekly report summarizing the reservation numbers. I will describe how that came about in 1-7.

![Figure 1-3a: Today stands out on the calendar *(The screen is in Japanese.)*](images/fig1-3a_calendar-today.png)

![Figure 1-3b: On the confirmation screen, the date and time appear large as "Today" *(The screen is in Japanese.)*](images/fig1-3b_confirm-today.png)

### 1-6 Too Many Plans to Choose From

Once the discount system was in place, I wanted next to increase the hours and plans that sell.

The 6 p.m. hour wasn't filling up, so I created a happy hour until 7 p.m. For people who come after eating, I created a drink-only plan with no meal. The course meal and cooking class, once held monthly, I turned into on-demand events that open when someone signs up, taken through the reservation site. To sell the time before opening on weekends, from 3:30 p.m., I created a party plan for groups of six or more.

Each one has a reason. The party plan, for example: if I made it look like a bargain on price, it would only draw in customers who had been choosing the standard plan, and sales would drop. So I placed the differentiation not on price but on the pre-opening hours, which had never brought in any sales. The happy hour discount makes no profit if combined with other discounts, so I decided it can't be combined.

And so the plans multiplied. Standard, Premium, Nice to Meet You, Welcome Back, Happy Hour, Drink Only, Course Meal, Cooking Class, Party. Each has conditions on party size, some accept discounts and some don't, and there are time restrictions.

One day I opened the reservation form and realized: customers can't choose with this.

I, the builder, understand every difference. But could someone opening the reservation site for the first time compare nine plans and their discount conditions and pick the one that suits them? If they can't, they give up partway through booking. The plans I worked to add could end up reducing reservations.

I could have tidied up. But every plan has a time I want to sell and a customer I want to see. I didn't want to cut any.

So I thought of a system where the customer consults the AI and decides on a plan. Tell it the party size, the date and time you'd like to come, and how you want to enjoy the evening, and the AI gives the suitable plan and price and takes you straight to booking. The shop shoulders the complexity of the plans. What remains for the customer is just a conversation.

This system is the "T-AI-MURO" I write about in 1-8. Before that, there is one more thing I noticed during this period.

![Figure 1-2: Plan selection on the reservation form. This many tabs are lined up *(The screen is in Japanese.)*](images/fig1-2_plan-tabs.png)

### 1-7 "Does This Actually Bring in Customers?"

On the day I added the party plan, I spent the whole day making one improvement after another to the reservation site. I tightened the header, matched the email design, and swapped out the AI that creates conversation topics for customers in the shop.

In the evening, a question suddenly came to me.

"Does this actually help bring in more customers?"

When I asked the AI, it honestly sorted that day's improvements.

| Category | That day's improvements |
| --- | --- |
| Things that may create new reservations | Party plan, the 3:30 p.m. slot on weekends and holidays |
| Things that raise the completion rate for people who came | Tightening the header, aligning the tabs |
| Things that encourage return visits | Unifying the email design |
| Things that don't help bring in customers | Switching the AI that creates conversation topics, the link to the next stop, the Agenda notice |

Of that day's improvements, only the party plan and the 3:30 p.m. slot led directly to bringing in customers. The rest were improvements to avoid losing the people who had already come. They matter too, but they don't increase customers.

There was a bigger problem. For none of the improvements did I have a way to measure whether it worked. There was no number connecting "I improved it" and "customers increased."

My answer was one phrase: "Let's build one."

So I set out to create a weekly customer-acquisition report. The number of reservations, number of guests, total amount, cancellations. Breakdowns by day of the week and by time of day. The ratio of first-time customers to returning ones. The counts for party and 3:30 p.m. slots. Where reservations came from (the reservation form, the chat window, reservations from AI, manual entries by the shop). Email click counts, and the number of reservations within seven days of those clicks.

Where there are numbers, time follows. On the same day, I had found another hole. I had set the cooking class and the party's 3:30 p.m. slot as "weekends," but when I wondered, "What happens on public holidays?" and looked into it, the reservation system had no concept of public holidays at all. On a holiday Monday the shop is open, yet the 3:30 p.m. slot didn't appear. I gave it a list of public holidays and fixed it to treat them like weekends. It was a hole that no one would notice until the person who built it did.

Before building the report, I plugged the holes related to time first.

Even regulars who had been coming since before I started using the reservation system look like "first-time customers" in the records. So in the report I write "first visit on record" and always attach the date the records began. To judge whether an improvement worked, you need the picture from before it. For the first report, I tallied back over the past eight weeks and used that as the baseline. In a week when the shop closed temporarily, for travel or other reasons, reservations naturally drop. So I also list the number of business days, so that comparisons can be made per business day.

The "Notable changes" section I stopped having the AI write, and made it follow fixed calculations and fixed sentences. This is to keep the weekly cost at zero. Customers' names and contact details do not appear in the report; only counts and ratios are shown.

Once I built a way to measure, the way I build improvements itself changed. I began deciding on an improvement and the method for measuring its effect together from the start. Measurement is not something to think about after an improvement; it goes in the same instruction document as the improvement. That is what I learned that day.

![Figure 1-6: The weekly customer-acquisition report that arrives each week (synthetic data) *(The screen is in Japanese.)*](images/fig1-6_weekly-report.png)

### 1-8 A Window That Talks with the Shop: "T-AI-MURO"

As I wrote in 1-6, the plans had multiplied, and the reservation form had become hard for a first-time visitor to choose from. And first-time customers want to know more than the plans and dates. What kind of atmosphere does the place have? Will I feel out of place alone? What kind of person is the owner? Is it okay to bring children? If you line up reservation buttons without answering questions like these, you can't give a hesitating person the push they need.

So I decided to put a "window that talks with the shop" on the reservation site. When a customer writes a question, the AI answers as the shop. If the number of people and the date get settled during the conversation, the customer can go straight to the reservation confirmation screen. It is called "T-AI-MURO," and in conversation it introduces itself as "Tamuro." T-AI-MURO speaks as the shop itself, and refers to the owner in the third person.

Customers hardly type anything. They just tap the choices T-AI-MURO offers, and the conversation moves forward. That means the choices it offers next decide the quality of the conversation. I always mix three kinds of moves into the choices: moves toward a reservation (number of people, price, open slots, date and time), moves toward getting to know the shop (atmosphere, the owner, who the customers are, whether you can talk with the person next to you), and moves that arise from the flow of the conversation. Getting people to a reservation is not the only goal. Letting them learn about the shop's atmosphere and the owner is also the heart of this window.

Only prices, I decided, would not be calculated by the AI. There is no guarantee the AI can correctly work out how discounts stack or how the steps by party size apply, every single time. The program produces prices and open slots with fixed calculations, and the AI sticks to the job of putting them into words.

#### The first knowledge came from my own past posts

For T-AI-MURO to answer questions about the shop, it needs knowledge of the shop. As the material, I exported all the posts I had written so far on Instagram and X (formerly Twitter) and used them. From them, I built the questions customers were likely to ask, and the answers.

When I actually tried it, X posts turned out to be more useful as material than Instagram. Instagram is mostly photos, with few words. On X, I had left written records, in my own words, about the food, the shop, and what I was thinking.

#### Only 9 of 36 passed

Before putting T-AI-MURO into production, I tested how correctly it could answer. I had AI run the tests too. I gave an AI playing the customer a character and a purpose, and had it talk with T-AI-MURO. I prepared 36 scenarios: "alone tonight," "4 people in two weeks," "with a child," "allergies," "private booking," "notice of being late," "the origin of the shop's name," "what kind of person the owner is," and so on.

The result of the first round: 9 passed out of 36.

The most common reply was "I'm sorry, I couldn't answer that well." This reply even came up for questions about the shop's atmosphere and the owner. Whenever words like "reservation," "today," "private booking," or "master" appeared, a list of open slots came up regardless of what the question was really about. In some conversations, a message about being late was taken as a new reservation. To a vegetarian customer, it gave stir-fried dishes with bonito flakes and miso soup as examples. It even gave information in English about a group purchase that we had already stopped.

#### I answered 11 questions with one line each

Part of the cause lay in how the program was built. I will leave that story for Chapter 2. The other cause was simple: the shop's facts were insufficient. An AI can't answer what it doesn't know.

So I collected the questions the AI couldn't answer and decided to answer them myself, one line each.

You can come in without a reservation. Children under elementary school age are difficult. Cancellations and changes by the day before, by email, phone, or social media message. For notice of lateness, please phone. There is a smoking area outside the shop. Bringing your own drinks is allowed with a corkage fee. Private booking is possible depending on price range and time, with a maximum of 19 people. Dietary restrictions and anniversaries we will accommodate as far as we can, so please consult us beforehand. The owner is in the shop almost every business day. A yukata festival is planned about once a year.

That's all. Just by answering 11 questions with one line each, 24 of 36 passed in the second test.

| Question | First answer | Second answer |
| --- | --- | --- |
| Is it okay with kids? | I'm sorry, I couldn't answer that well | Elementary school age and older can be accommodated if you consult us. Under elementary school age is difficult |
| Can I get in without a reservation? | (list of open slots) | You can come in without a reservation |
| Is the master in today? | (list of open slots) | The owner is in the shop almost every business day. Today is a business day, so they plan to be in |
| Is it a quiet place? All regulars? | I'm sorry, I couldn't answer that well | It's a place to relax. Conversation between customers comes easily, and it isn't a rowdy place |

Here a pattern began to emerge. The AI creates the questions we expect, T-AI-MURO answers them, and we fix the mistakes. Then only the questions that can't be answered because the shop's facts are missing get passed to the owner. The owner's effort is just one line for each unanswerable question. Everything else, the AI runs.

#### The scene where "budget ¥5,000 (about $33)" failed

I had attached an AI verdict to the AI tests too. A different AI reads the conversation log and decides pass or fail.

Among them was a scenario with a customer whose "budget is ¥5,000 (about $33)." The AI's verdict was a pass. T-AI-MURO had politely presented plans within the budget.

But when I read it, it was a fail. It hadn't asked the number of people. Tamuro has a group discount. Depending on the party size, the plans you can choose for the same budget change.

At that point, I restated the purpose.

"Aim for as large a group as possible, so that the total amount comes in. Confirm the number of people. The final goal is to get customers to come. The more, the better. To raise sales."

With that single statement, the whole design of the conversation changed. Always confirm the number of people before answering about prices, and answer with the total amount. Just before a step in the group discount, add "one more person gets you what percent off." When a budget is given, show the top plan within the budget first. However, customers who come alone make up half of the shop, so for a customer of one, don't suggest increasing the party size.

When you have AI run the AI tests, they run fast. But it is a human who decides the standard for passing. Whether you can state the purpose in one sentence. That decided the quality of the AI's conversations.

#### The customer's wishes take priority over the shop's recommendations

There was one more scene where I drew an important line.

During testing, I found a problem: every reservation was being handed off to the cheapest plan. When I fixed it, this time almost all became the Standard plan, and the average total amount jumped to about double. I was nearly delighted, but looking closely, the customer-playing AI had simply been pressing the first choice every time. Even customers who said "the cheapest is fine" were being recommended Standard.

Here I set a principle. What the customer clearly states as a wish (the cheapest option, a budget, the name of a plan) always takes priority over the shop's recommendation. The shop's recommendation is only for when the customer hasn't said anything.

The shop's aim of raising sales and the customer's trust can collide over a single way of recommending. If trust is lost, visits themselves decrease. It was the owner, not the AI, who could draw this line.

Later, when I retrained T-AI-MURO with a large number of questions, the most common cause of mistakes was "reacting to words and making a fixed move before answering the question." The moment it heard words like "number of people," "how much," or "alone," it skipped the question and went to the reservation flow or recommendations. In terms of service, it's a clerk who pushes a sale without listening to the customer. Answering the customer's question first. This basic of hospitality was the biggest challenge even for AI.

On the night of October 6, 2026, T-AI-MURO appeared at the top of the reservation site as the real entrance. Since some customers don't want to book by conversation, I've kept the previous reservation form alongside it.

> Try it: Open Tamuro's reservation site (https://tamuroreservation.vercel.app/?src=b2-en-kindle) and ask T-AI-MURO "alone tonight." The conversation takes you through to today's availability and prices.

![Figure 1-4: The T-AI-MURO conversation screen. The conversation moves forward just by tapping choices *(The screen is in Japanese.)*](images/fig1-4_talk.png)

![Figure 1-10: Questions it couldn't answer pile up in the admin screen (synthetic data) *(The screen is in Japanese.)*](images/_trim/fig1-10_unanswered.png)

### 1-9 And Then, from the Customer's AI

By building T-AI-MURO, Tamuro's reservation site gained the ability to "answer questions about the shop in conversation, show prices and open slots, and guide people through to a reservation."

What I thought of next was making it possible to do the same thing from the customers' own AI.

T-AI-MURO can only talk with people who come to Tamuro's reservation site. But many people consult the AI they use every day first. If that AI doesn't know about Tamuro, Tamuro won't even make the list of candidates. Instead of waiting for customers to come to Tamuro's site, open Tamuro's window on the customer's AI side. That is the MCP server.

To be honest, I hesitated at first about building this. At this point, not many people book restaurants from their own AI. Judging that I couldn't expect a direct increase in reservations, I once lowered its priority and put it on hold.

I decided to build it anyway because I thought it was only a matter of time before the entrance changes. As I wrote at the start, in August 2026 it became possible to make reservations from ChatGPT through a major reservation service. Sooner or later, having AI find a restaurant for you will be the norm. When that happens, small shops that aren't listed on the big services will drop out of the AI's sight. So, open the window before the entrance changes.

What I decided for the first version was very narrow. It only needed to do the same as the conversation window on the reservation site (T-AI-MURO). All it can do is read the shop's information, open slots, and prices, and hand over the URL of a reservation page with the conditions filled in. Confirming the reservation is done by the customer themselves on Tamuro's page. The customer's AI doesn't confirm a reservation on its own. The final push is made by a person.

Let's go back to the opening scene.

On a Friday evening, a customer asks their own AI, "Is there a place in Higashi-Nakano where I can drink alone tonight?" The AI queries Tamuro's window. Tamuro's reservation system returns tonight's open slots, plus the plan and price that suit a solo customer. The AI tells the customer, and offers a Tamuro reservation page with the date, time, and number of people filled in.

Everything I've written about in this chapter supports this series of steps. The discount system built along with the price increase. The system that nurtures regulars. The data that showed most reservations are made on the day. The shop knowledge grown by answering 11 questions one line each. The principle of putting the customer's wishes ahead of the shop's recommendations.

A shop that gets booked through AI wasn't built overnight. It stands on the accumulation of small systems added one at a time, tested, discarded, and fixed.

> Try it: Register Tamuro's MCP server (https://tamuroreservation.vercel.app/api/mcp) with your own AI and ask, "Is Tamuro open tonight?" How to register is written in the Afterword.

### 1-10 What We Built, and What Worked

In this chapter, I've talked about building many systems. But "we were able to build it" and "the business changed" are different things. At the end of the chapter, I'll separate the two.

What could be confirmed with numbers. That 88.1% of reservations are for the same day. That the pass rate of the conversation window rose from 9 to 24 just by adding 11 items of the shop's facts. That the pass rate for price and plan guidance rose from 29.4% to 42.7% after fixes. These are facts on record.

What feels like it's working, but where I can't prove causation. That more customers come in groups using the group discount. That the first-time/welcome-back plan is being chosen. That the topic of the confirmation email has become part of the conversation at the counter. I feel it on the floor, but I can't say "they wouldn't have come without that system."

What has been built, but whose effect I still don't know. How many more advance reservations the early-booking discount will bring. How many reservations will actually come in from MCP. I've only just started measuring with the weekly report, and the numbers will be in later.

Look separately at the amazement of "we could build this much with AI" and the result of "how did that change the business." Without this distinction, building itself becomes the goal. I nearly fell into that myself once (as I wrote in 1-7).

The story of what's behind this reservation system, the technology, continues in Chapter 2. If you aren't interested in technology, skip to Chapter 3. There I talk about how the small tools born around this reservation system are being handed out to other shops too.

## Chapter 2: Technology - Behind the Reservation System

Key points of this chapter

- The quality of the AI's conversations was decided less by the AI's cleverness than by "the shop facts we hand over" and "whether a program overrides the AI's replies on its own"
- The reservation system I built by feel still had a hole that let customers' personal information be read from outside, and zero automated tests. I had AI audit it to find these, and had AI fix them
- From that reflection, I changed how I build: define requirements in detail before building, and hand the AI the specification itself to implement

(This chapter has a lot of technical terms. If you aren't interested in technology, you can skip to Chapter 3 and the story still connects.)

### 2-1 How the MCP Server Works

MCP (Model Context Protocol) is a common set of conventions for AI to use outside tools and data. Proposed by Anthropic, it is now supported by many AIs, including ChatGPT and Claude.

To put it in an analogy, MCP is a standard for power outlets, for AI. Because the shape of the outlet is fixed, appliances from any maker work when plugged in. In the same way, if you build a window to match the shape of MCP, any AI can use that window.

An MCP server tells the AI "what you can do through this window." Tamuro's MCP server, for example, lines up tools like the following.

- Read the shop's information (business hours, number of seats, house rules, atmosphere)
- Read plans and prices (the result of calculating discounts by party size and date)
- Read open slots (the times available for booking on a specified day)
- Create the URL of a reservation page with the conditions filled in

When a customer asks their own AI, "Is Tamuro open tonight?", the AI connects to Tamuro's MCP server, chooses "read open slots" from the lined-up tools, and calls it. Tamuro's server returns the result, and the AI puts it into words for the customer.

What matters is that the AI doesn't confirm reservations on its own. In the first version, I deliberately left reservation confirmation out of the tools. All the AI can do is read, and guide people to a reservation page with the conditions filled in. The confirm button is pressed by the customer themselves on Tamuro's page. The danger of the AI creating large numbers of mistaken or prank reservations is avoided by design from the start.

Price calculation uses the same calculation mechanism as the reservation site. The prices shown on the reservation form, in the conversation window, and through MCP all come out of the same single program. This is the other meaning of the task I'll write about later, "consolidating the discount calculation in one place."

![Figure 2-1: From the customer's AI to Tamuro's reservation page. The customer presses the confirm button](images/fig2-1_mcp.png)

### 2-2 How the Conversation Window "T-AI-MURO" Works

#### Prices from the program, words from the AI

T-AI-MURO splits the roles in two. The program produces prices and open slots with fixed calculations, and the AI puts them into words for the customer.

AI is good at producing text, but there is no guarantee it calculates correctly every time. How discounts stack, steps by party size, the number of days for the early-booking discount, whether it can be combined with happy hour. If you leave all these rules to the AI, it will surely get something wrong somewhere. And a mistake in price damages the customer's trust most of all.

So, the parts that must not be wrong go to the program, and the parts that convey things softly go to the AI. This division is the first principle in building the conversation window.

#### For a small shop, you don't need RAG

To have the AI answer about the shop, you need to hand the shop's knowledge to the AI. A commonly used method is RAG (retrieval-augmented generation). You cut the knowledge into small pieces and store them, and each time a question comes in, you find only the parts that seem relevant and hand them to the AI. When the knowledge is vast, this method is indispensable.

But Tamuro's knowledge isn't that large. The shop's history, the food, the rules, the atmosphere, the owner's thinking. All together, it fits easily within what the AI can read at one time.

So at Tamuro I chose to have the AI read the whole text of the shop's knowledge every time. There's no need to build a search mechanism as RAG requires, and nothing gets missed in searching. At first I planned to reuse a RAG mechanism, but partway through I switched to the full-text approach.

Having it read the whole text every time costs more in AI fees. So I use a mechanism that reuses the same text to lower input costs (prompt caching: instead of making the AI reread the same preamble every time, it remembers what it has already read). It's enough to bring in RAG once the knowledge grows large.

#### A program that overrides replies on its own

In Chapter 1, I wrote that only 9 of 36 passed in the first test. Part of the cause lay in how the program was built.

When I investigated, I found a mechanism left in place where the program judged the reply the AI had made by keywords and swapped it for a fixed sentence. When words like "reservation" or "today" appeared, it threw away the AI's reply and swapped in a list of open slots. Even when the AI answered correctly, it never reached the customer.

Furthermore, I found that the main body of the shop's knowledge (33 sections) wasn't included in the instructions to the AI. The AI had been answering without knowing about the shop.

The quality of the AI's conversations was decided less by the AI's own cleverness than by the shop facts handed over and by whether a program overrode the AI's replies on its own.

#### Fill in the expected Q&A by counting

I increased the test scenarios from the first 36 to 110, and then to 355. But if people add scenarios by whim, there's no way to know whether anything is missing. To the question "Is this comprehensive?", the honest answer was "No, it isn't."

So rather than expanding coverage by imagination, I made it a matter of counting by machine the places not yet passed through, and filling them in. For four things: the 33 sections of the shop's knowledge, the transitions between choices, the steps of the discounts, and combinations of time slots and days of the week. I count how many times each was passed through in testing, and automatically add scenarios where the count is zero.

I also used a method of crossing six axes (party size, purpose, way of drinking, date and time, phrasing, menu) and creating scenarios so that every pair of two combinations is passed through at least once.

I also found a hole around time. "Today" and "from now" are determined by the actual time the test runs, so results from running at noon and running at night differ. So I fixed the clock during testing and made it run at five points in time: before opening, during business hours, just before closing, on a regular day off, and on a holiday.

The AI's answers vary slightly each time, even to the same question. For scenarios directly tied to sales, I set the condition that they must pass all three times when run three times.

#### When a bad number comes out, suspect the test first

In the test that ran 355 scenarios at 5 points in time, of 1,775 conversations, 28.5% passed.

Instead of starting to fix things right away, I first separated out: "Is this number really a weakness of T-AI-MURO, or is the test wrong?" If you fix things while the test is wrong, you end up "fixing" even the correct answers.

| Cause of error | Count |
| --- | --- |
| A fixed sentence hijacks the question | 276 |
| Doesn't answer the question, moves to the reservation flow or recommendations | 266 |
| Test environment failure (T-AI-MURO couldn't produce a reply because of the cost cap) | 211 |
| Errors in dates, days of the week, holidays, days off | 142 |
| Inventing or asserting facts the shop doesn't have, promising to pass on messages | 119 |

The top two shared the same root: "reacting to words and making a fixed move before answering the customer's question." The 211 in third place were not T-AI-MURO's errors. The cost cap was reached partway through the test, and T-AI-MURO simply couldn't produce replies. Excluding these, the pass rate becomes 32.4%.

The judging AI can also make mistakes. When I pulled out 20 cases and checked them, 2 were errors on the test's side. In one of them, the judge didn't know that "this reservation site has member registration." The judge also doesn't know anything beyond the materials it was given. The accuracy of the test is decided by the completeness of the shop's rules handed to the judge.

In the retest after fixes, the pass rate for price and plan guidance rose from 29.4% to 42.7%. I haven't yet run the final test that passes every case through again. To keep costs down, I've decided that the all-cases test is run only once, before putting a major change into production. The pass rate is still being raised even as I write this book.

#### The test stopped production

AI tests cost money. The first 36-scenario test cost about ¥426 (about $2.8). Most of it went to the "thinking effort" of the customer-playing AI, and when I turned that off, 3 scenarios cost about ¥6 (about $0.04).

But then one day, partway through a test, the AI usage balance ran out and everything stopped. In a single day I had used about 35 million tokens (the unit of text an AI reads and writes). The cause was running the 221-scenario test over and over, and running scenarios tied directly to sales four times each.

What was frightening was that the test and production used the same wallet. When the balance runs out, even the production conversation window stops. On another day, this time I hit a monthly cap I had set myself, and the production conversation window and the AI that creates conversation topics for customers in the shop stopped at the same time.

The real danger of a testing budget was not the bill, but that production was using the same wallet.

From there the rules changed. Do the checks that cost nothing (program tests and automatic screen checks) first. Limit the AI-calling tests to those related to what was fixed. Run the all-cases test only once, before going to production. Write the estimated cost and a cap in the instructions, and stop if it looks likely to be reached. To keep funds for production, stop testing when the organization-wide usage gets close to the cap.

There was also a lesson in how costs swell. Once, the judging AI's cost came to 2.6 times the estimate. The cause was that the long preamble handed to the judge every time (the shop's knowledge and rules) wasn't being reused, so a rewrite charge was incurred each time. When I fixed it to write the preamble in once and reuse it, the cost per conversation dropped to about a third. AI cost swells not with how many times you call it, but with how many times you rewrite the same preamble.

The same 221-scenario full test came down from about ¥1,040 (about $6.9) to about ¥400 (about $2.7) through repeated improvements. I replaced the customer-playing AI with a fixed script, and split the information handed to the AI into a "core sent every time" and "sections read only when needed."

Because of budget constraints, the design changed toward increasing the parts that can be checked at zero cost, that is, the parts decided by the program. As a result, accuracy rose too. Money changes design.

![Figure 2-2: Results of the AI tests. The pass rate and a breakdown of the causes of errors](images/fig2-2_test-result.png)

### 2-3 Having AI Audit What I Built

#### Customers' names could be read from outside

In August 2026, while I was reviewing how the reservation system worked, I made a discovery that sent a chill down my spine.

Customers' reservation data could be read by anyone from outside. Names, phone numbers, email addresses, the requests field. Everything entered into a reservation could be pulled in full, with no authentication.

There is something I should say honestly. It is true that the data could be read from outside. At the time, the reservation site had very little traffic, and I believe it is unlikely anyone actually read it. But I have no record that could prove it was not read. "It could have been retrieved" and "it was actually retrieved" are two different things, but the former alone was a serious failure for a shop.

When I traced the cause, it came down to how the reservation form was built. To calculate open seats, the form loaded 35 days of reservation data directly from the screen. If the screen can read it, then anyone who knows how screens like that are built can read the same data. It was the result of a first foundation built by feel, one that reached the goal of "show the open seats" by the shortest route.

I also found that the email address for notifying the shop's administrator was public, and that anyone could write to the place where translations were stored, which meant the data could be vandalized or the costs inflated.

The order of the fix mattered. If I banned reading all at once, the reservation form could no longer show open seats and would stop working. So first I moved the open-seat calculation to a server-side endpoint. Next I changed the reservation-complete screen so that it also gets only the information it needs from the server. Last, I closed off reading from outside. I made the fix in four stages in this order and applied it to production.

After the fix, I used a machine to check that it was really closed. I prepared a test that tries to read reservation data without authentication, and I run it automatically after every change to confirm it is always refused. I did not fix it once and call it done. I set it up so that a check keeps watch to make sure it never opens again.

#### Real customer data was left in the development history

Then I had the AI audit the whole repository (the storage place for the program), and a more serious problem came up.

During development, a file containing real customers' data (email addresses and phone numbers from 55 reservations) had been sent to the repository, still included in the program's change history. The repository was private, but since it remained in the record, I could not leave it alone.

I removed the file from the entire change history, rewrote the history, and stored it again. Even so, the old records from before the rewrite might still remain on the side of GitHub, which hosts the repository. So I asked GitHub support to delete them, and confirmed it was done.

The audit also found other problems: the translation endpoint could be used without authentication, the administrator login could be attacked by brute force, and there was a window of time in which, if payment were re-enabled, a reservation could be confirmed while still unpaid. I fixed them one by one, starting with the most serious.

#### There were zero automated tests

The audit revealed one more fact. The reservation system had not a single automated test.

Automated tests are a mechanism in which a machine automatically checks whether the program works correctly. Without tests, when you fix something, you have no way to check whether something else has broken. Every time you add a feature, somewhere something quietly breaks. That was exactly the state of things during the period when I was building by feel.

So I rebuilt the testing foundation from zero. I introduced a system (CI) that automatically runs four checks after every change: type checking, style checking, tests, and the build. Important decisions such as price calculation, reservation judgment, linking members, and issuing coupons were separated from the screen programs so that they can be verified on their own. The rules for reading and writing the database are also checked in a test environment that imitates a real database. The unit tests started at 275 and later grew past 500.

There is one condition I always impose on tests: "break it, and confirm it fails." Even when a test turns green (passes), you do not know whether that test can really catch a problem. Only after I deliberately break the program and confirm that the test turns red (fails) do I trust the test. That is because tests written by AI sometimes check nothing at all.

#### Eight holes in the reservation form

After the testing foundation was in place, I had the AI examine the whole reservation flow again. It found eight problems that did real harm.

The most serious was that pressing the submit button repeatedly created a double reservation. This was actually happening in production. I fixed it with a mechanism that processes the same action only once even if it arrives twice (idempotency). The other problems were these: a reservation could not be confirmed if information about a deleted menu item remained; there was a gap in the full-house check that left room to exceed capacity; nobody noticed when a confirmation email failed to send; input was not validated on the server side; internal wording appeared on screen when an error occurred; the text in input fields was so small that the screen zoomed in on its own on iPhone; and autofill for input did not work.

For email failures, I made it possible to detect them in the admin screen and resend. During that investigation, I also found that the audit log that records reservation confirmations had been failing every time, from well before the fix, and had recorded nothing.

I fixed these one by one and applied them to production.

#### Never skip verifying code the AI wrote

What I learned from this experience is that precisely because a program was written by AI, you must not skip verification.

AI quickly gives shape to what it is told. But consideration for things it is not told, such as "make it unreadable from outside" or "treat a double submission as one," does not get in unless you instruct it. And holes like these lie quietly inside programs that look like they are working.

People do not need to read all the code. The correctness of the program is watched by machine checks and by an audit from another AI. Whether the result fits the shop's purpose is watched by the owner. You do not need to read it, but you must not skip verification. That is what I believe it means to build with an agent-type AI.

![Figure 2-3: The rules when it could be read from outside, and the rules after the fix (excerpt) *(The screen is in Japanese.)*](images/fig2-3_rules-before-after.png)

### 2-4 Building by Feel Multiplies Contradictions

The more features I added, the more parts there were that clashed with what I had decided earlier.

The typical case was the discount calculation. In the reservation form, the confirmation screen, the email, and the admin screen, the discount calculation was written separately in each place. If I changed a discount rule in one place, another place kept calculating with the old rule. For the same reservation, the screen and the email could show different amounts.

Later, I gathered the price calculation into a single file. The reservation form, the chat window, and the MCP server all produce prices from there.

The rules for stacking discounts also changed along the way. As I wrote in Chapter 1, happy hour was originally going to be combinable with other discounts, but I found it would not turn a profit and changed it to non-combinable. Every time a rule changed, a person had to remember where to fix things. That was the weakness of a system built by feel.

There was also a mismatch between the test environment and production. While testing the chat window, a question, "Wasn't there something like 10% off?", revealed that the discount rules in the test environment had drifted from production. If the values in the test environment differ from production, you can pass the tests and still be wrong in production. What I decided then was the principle that "production is correct." Since then, before every test run, I copy the production settings into the test environment and confirm that the mismatch is zero before running.

AI builds what it is told. But it does not notice contradictions with earlier decisions. What prevents contradictions is not the AI. It is deciding things beforehand.

### 2-5 Relearning Requirements Definition

After reflecting on the reservation system I built by feel, I relearned requirements definition. Requirements definition means deciding, before you build, what you will build, what you will not build, and who will use it and how, and writing it down in a document.

It was something I did as a matter of course back when I was a systems engineer. But once I could build with AI, I had skipped it without noticing. Tell it an idea and something working appears in minutes. In that speed, I had cut the effort of deciding.

My way of building now has three stages.

1. First, decide the requirements in detail. What to build, what not to build, who will use it. The behavior of each screen. How to handle exceptions (errors, double presses, expiry). Rules that easily end up contradicting each other later, like prices and discounts, I decide in particular detail. I do this work too in dialogue with the chat AI. I have the AI find holes and contradictions ahead of time, and the owner decides.
2. Write what was decided as a "requirements document." Not spoken or on-the-spot instructions, but gathered into one document. This becomes the only standard for checking later what is correct.
3. Hand the whole document to the AI and have it implement. I give the whole document to the AI that writes the program (Claude Code), together with the conditions for passing (all tests pass, check in the test environment before production, and so on). The AI builds on its own until it meets the conditions, and checks on its own. The owner looks only when it stops partway and at the final check.

For example, the requirements document for the chat window "T-AI-MURO" was rewritten from the first version through the third. In the second version I decided "do not let the AI calculate prices," "put the shop's knowledge and the price calculation into one window," and "keep the form too, for people who do not want to reserve by chat." In the third version I decided "where to keep the master copy of the shop's knowledge," "this window alone shows open slots," "make the first exchange a four-choice question," and "do not save conversation logs; store only the questions that could not be answered." Because the decisions remain in a document, I can trace later why things are the way they are.

With this way of building, even when I add features, I can notice contradictions right away by checking against the document. Precisely in an age when AI does the building, the "power to decide" before building is needed. That was the biggest lesson I learned from the reservation system.

I also built a mechanism that puts the procedure itself into a document and hands it to the AI, so this way of building can be run the same way each time I launch a new product. I will write about that in Chapter 4.

![Figure 2-4: Table of contents of the T-AI-MURO requirements document (version 3) *(The screen is in Japanese.)*](images/fig2-4_requirements.png)

### 2-6 Learning the Language of UI

There is one more thing I relearned: the names of screen components.

Even when I told the AI "do this here," the screen often did not come out as I expected. When I thought about the cause, I found that I did not know the names of the screen components. Even if I described "a small window that appears on top" or "a notice that disappears in a few seconds," it was hard for the AI to tell what I meant.

So I read a reference book on UI (user interface, the look and operation of a screen) and learned the names of components and the technical terms of design.

| Component | What it is |
| --- | --- |
| Modal | A small window that appears over the screen. You cannot operate the screen behind it until you close it |
| Toast | A notification that appears at the edge of the screen for a few seconds and disappears on its own |
| Tab | A mechanism where pressing a heading switches the contents |
| Accordion | A mechanism where pressing a heading opens and closes the contents |
| Drawer | A menu that slides out from the side of the screen like a drawer |
| Others | Breadcrumbs (a trail showing where you are now), carousels (items you scroll sideways), bottom sheets (a panel that rises from the bottom of the screen), and so on. Each name you learn lets you instruct the AI in a single phrase |

When you communicate by name, the screens the AI produces get close in one try. If you say, "Show the reservation confirmation screen as a modal," the AI does not hesitate.

#### AI swings to extremes between adding and cutting

Even after I learned the words, building screens with AI had a different kind of difficulty. AI swings widely.

When I asked for a "stylish" header on the reservation site, I got an impressive, thick header. But the whole point of a reservation site is reservations. For regulars who book every time, a thick header with long explanations is just a nuisance. I had it cut the vertical length by about half, keeping the same amount of information.

When I standardized the email footer and added a link to the Next Stop Guide, the body text now looked plain and shabby by comparison. So I added a heading, a table of key points, and one button to press to the body as well. When I added an entrance to the chat window in the footer, it looked cluttered. When I squeezed it into two lines of links separated by rules, it was tidy but inconspicuous. In the end it settled on two cards that show the role by "when to use it." The left is "for your next reservation," the right is "after your meal."

Too thick, too trimmed, too prominent. What decided the right spot was the owner's word each time.

#### A design proposal with no pictures

This happened too. I asked the AI that writes programs to create improvement proposals for the chat window using a design AI (Claude Design), and a report came back saying, "I made proposals for eight screens." But when I opened it, there was only text description. The AI had not been able to draw pictures, yet only the report "done" remained.

In the end, the chat-side AI drew four proposals directly in the design screen. It picked up the colors of the current screen from a screenshot, put the shop's history in a timeline, split the flavoring into two frames, "cooking method" and "taste," made plans into explanation cards, and unified prices into a reservation summary.

When you have AI run a test, it says "passed." When you ask AI for a design, it says "done." Checking what is inside is a human's job. The standard for judging is something only humans can keep holding.

#### What you can take away from this chapter

- Building something that works and being able to run it safely are different things.
- Check AI output not by the AI's words but by tests. A test can be trusted only once you have checked that it fails when you break things.
- Calculations that must not be wrong, like prices, should not be left to the AI's text generation. Give them to the program.

The continuation of this chapter (newly found holes and the steps I took to fix them) is on note and X. note <https://note.com/bontallc> / X <https://x.com/tamuro_hnakano>

## Chapter 3: Distributing My Shop's Tools to Other Shops

### 3-1 The Small Green Sign on the Reservation Page

Open Tamuro's reservation page and you will see a small green sign near the top. While the shop is open it says "OPEN," and when it closes it says "CLOSED." When the owner presses the extend button, the closing time moves back 30 minutes and a touch of vermilion appears on the sign.

Independent restaurants share one trait. They open almost exactly on time, but closing often runs late. If the conversation with customers is lively, the shop lights stay on past the 10:30 p.m. last order.

But from the customer's side, you cannot see that. The "Open" display on Google Maps is judged only from the hours registered, so it reflects neither extensions, nor early closings, nor temporary closures. Nobody walks to a shop past its closing time thinking, "Maybe it's still open." Calling to check feels awkward too.

This sign is a tool that answers that "Is it still open?" It is called "AgendaLuce (Light Notebook)." Luce means "light" in Italian.

The Light Notebook is built to run with almost no attention from the owner. Register the opening and closing times for each day of the week once, and the sign turns on and off automatically. The owner touches it only when extending, closing early, or taking a day off. To extend, you press one button on your smartphone. Staff can also operate it from a dedicated link that works without logging in.

Customers need no login or registration. Open the public page and you can see the current state of the light. If you add it to your smartphone's home screen, it works like an app. The small sign component can also be embedded in other websites. What appears on Tamuro's reservation page is that component.

The Light Notebook is free. If you only embed the sign component in your website, setup takes about 10 minutes.

And here is the important part. This Light Notebook is not only for Tamuro. Any shop can use it.

I deliberately left the shop name out of the sign's design. If I put a name on it, it would become a sign for Tamuro. You can also choose the display language. I made the component small so it can be embedded in any shop's website.

A tool born from Tamuro's problem of "closing runs late," made from the start in a form anyone can use. That is the Light Notebook. And the collection of tools like it is the "Agenda series."

![Figure 3-1a: The Light Notebook sign on top of the reservation page (open) *(The screen is in Japanese.)*](images/fig3-1a_luce-open.png)

![Figure 3-1b: A touch of vermilion appears during an extension *(The screen is in Japanese.)*](images/fig3-1b_luce-extended.png)

![Figure 3-6a: The owner's screen. To extend, press the button once *(The screen is in Japanese.)*](images/fig3-6a_luce-admin.png)

![Figure 3-6b: Right after pressing extend. The closing time moves back 30 minutes *(The screen is in Japanese.)*](images/fig3-6b_luce-admin-extended.png)

![Figure 3-6c: The public page customers see (during an extension) *(The screen is in Japanese.)*](images/fig3-6c_luce-public.png)

### 3-2 It Began with the Black Leather Notebook

The Agenda series was not planned as a series. It began with a single system, one that has not even been released yet.

What I first set out to build was a mechanism that recognizes customers' faces and welcomes regulars. A camera at the shop entrance tells visitors apart by face and lets the owner know: "That's the person who had the tonteki last time, the one we haven't seen for three months." I meant to have a machine help with the job a small shop's owner does in their head: remembering faces, names, and preferences.

But soon after I started building, I realized this was a system entrusted with something very heavy. Faces. Attributes. Visit history. A customer's character. All of it is information that can never be taken back once it leaks.

What came to my mind then was Seicho Matsumoto's "Black Leather Notebook." A record shown to no one, yet certainly existing. A ledger that, once opened, sets people's lives and deaths in motion. Isn't that exactly what I am trying to build?

In Italian, "notebook" is Agenda, and "black" is Nera. Put together: AgendaNera. The black leather notebook. That is how the name was decided first.

AgendaNera is still being built. It is the one I am building most carefully in the series.

And this naming was the trigger. If there is a black notebook, there can be notebooks of other colors. I would rebuild the mechanisms I used every day in my own shop into forms any shop can use, and release them one notebook at a time. That is the [Agenda series](https://bontallc.com/agenda?via=b2-en-kindle).

### 3-3 Adding Notebooks, One at a Time

The Agenda series is a collection of small web apps, each answering one problem of a restaurant with one tool. Each has an Italian name and a Japanese nickname ending in "notebook." Each name has its own origin.

| Name | Nickname | Origin of the name | What it does |
| --- | --- | --- | --- |
| AgendaTimbro | Time Clock | Timbro means "stamp." It is the clock-in itself | Records staff clock-in and clock-out |
| AgendaOro | Profit Planner | Oro means "gold." The money notebook | Estimates profitability for opening a shop or a new menu item (free) |
| AgendaBis | Next Stop Guide | Bis means "encore." The "Bis!" shouted from the audience at a concert | Guides customers to a nearby next stop (free) |
| AgendaQA | Support Guide | Qua means "here." When in trouble, here | The series' shared help desk (free) |
| AgendaLuce | Light Notebook | Luce means "light" | Shows whether the shop is open (free) |
| AgendaRicetta | Recipe Costing | Ricetta means "recipe" | Works out a recipe's cost and cost ratio (free) |
| AgendaNera | Regulars Notebook | Nera means "black." The black leather notebook | Welcomes regulars with face recognition (under construction) |
| AgendaTurno | Shift Roster | Turno is Italian for "turn" or "duty shift" | Collects staff shift requests and hands out the schedule that the owner's own AI puts together (coming soon) |

Which notebook suits which kind of shop? The Time Clock is for shops with two or more staff who manage attendance on paper or in LINE *(Japan's most widely used messaging app)*. The Profit Planner is for people about to open a shop, and for those who want to review their numbers because rent or costs have changed. The Next Stop Guide is for shops centered on meals that want to send customers on to the next place early. The Light Notebook is for independent shops whose closing runs later or earlier than planned. Recipe Costing is for shops where the recipes are in your head but you have never worked out a cost ratio.

#### The Time Clock does not calculate payroll

The Time Clock turns the shop's tablet or the staff's smartphones into a clock-in machine as they are. Just tap your name. The attendance sheet is tallied automatically and can be exported as CSV (a format that opens in spreadsheet software). The business day starts at 5 a.m., so even with late-night hours the date does not roll over.

But this Time Clock deliberately does not calculate payroll.

Hourly wages, allowances, and cutoff dates differ too much from shop to shop. Late night at 25% extra, holidays as a separate category, transportation by daily amount. However I built it, it would not fit someone's shop.

So instead of calculating, I prepared "a template of instructions to hand to an AI." The owner pastes the downloaded attendance CSV and this template, as they are, into whatever AI they normally use, whether ChatGPT, Claude, or Gemini. Then the AI calculates late-night premiums, holiday pay, and transportation and lists them out. Each shop's rules, like "we close the books at month end, late night is 25% extra, and Sundays are a separate category," can be added to the template and will be reflected as they are. The CSV includes columns for the day of the week and the holiday name so that the AI can calculate correctly.

I do not hold the calculation mechanism myself; each shop keeps its own rules in its own hands. I figured that is the hardest way to break.

#### Guide them to a next stop, and leave your own shop in their memory

The Next Stop Guide is a tool for making a "next stop guide page" to give to customers. To customers who have finished their meal, it guides them to a nearby bar or a place for a final bite, along with how many minutes it takes on foot.

It looks like a tool for sending customers elsewhere, but there is a small trick in it. Guiding someone to a second stop implies that the first stop was your shop. While appearing to send customers away, it is actually engraving "the first stop was this shop" in their memory. That is how it is designed.

#### Three design principles: automatic, borrowed strength, single function

All the notebooks in the Agenda series share three principles.

The first is "automatic." It should run without the owner touching it every day. With the Light Notebook, once you register the schedule, the light turns on and off by itself. A restaurant owner has no time to touch a screen during service. A tool that does not work unless you touch it will eventually go unused.

The second is "borrowed strength." Do not build everything yourself; leave things to the tools and AI the owner already uses. The Time Clock's payroll is the model case. The shift notebook is the same: it handles only collecting the staff's preferences, and leaves the work of building the shifts to the owner's own AI. It does not carry a complicated mechanism of its own, nor the cost of calling an AI. That is why the price can be kept low.

The third is "single function." One notebook does only one thing, reliably. A multifunction system is too heavy for an independent shop. Keep adding features and it gets harder to use, and the contradictions on the builder's side multiply. That is what I learned firsthand through the reservation system in Chapter 2. So I add notebooks one at a time, each one doing "just this one thing properly."

#### Why the reservation system is not in the series

At this point, I expect an obvious question. The thing Tamuro put the most work into is the reservation system. Why not put it in the Agenda series?

In fact, I once intended to. The plan was to put the reservation system into a form other restaurants could use, and release it as one notebook of the series. But in August 2026, I called that plan off.

The reason is exactly what I wrote about in Chapter 1. Tamuro's reservation system is packed with Tamuro's way of doing business. That solo diners make up half of the customers. That nearly 90% of reservations are made the same day. That I want to sell the time before opening. That I want people to come in groups. That I want to grow regulars. I built the discount combinations, the order of the emails, and the way the chat recommends things all to fit these.

If I thinned it out into something anyone could use, it would become an ordinary reservation system that fits every shop so-so. Then Tamuro's strength would vanish. The reservation system and CRM are the shop's way of selling itself. Rather than fitting the shop to a generic system, fit the shop's system to the shop. Our shop, on our own specifications. So I decided to keep Tamuro's reservation system as Tamuro's alone.

So is there nothing to give out beyond the shop? No. Around the reservation system there are many small problems common to every shop. Keep the core of the shop on your own specifications. Build the tools that solve the surrounding problems in a form everyone can use from the start, and give them out. Tamuro's reservation page is a sample with both lined up on a single screen. On top of a reservation system just for Tamuro sits the Light Notebook sign that anyone can use.

![Figure 3-2: The Agenda series introduction page *(The screen is in Japanese.)*](images/fig3-2_agenda-lp.png)

![Figure 3-3a: Introduction to the Time Clock *(The screen is in Japanese.)*](images/fig3-3a_timbro.png)

![Figure 3-3b: Introduction to the Profit Planner *(The screen is in Japanese.)*](images/fig3-3b_oro.png)

![Figure 3-3c: Introduction to the Next Stop Guide *(The screen is in Japanese.)*](images/fig3-3c_bis.png)

![Figure 3-4: The Time Clock's clock-in screen. Just tap your name (synthetic data) *(The screen is in Japanese.)*](images/fig3-4_timbro-kiosk.png)

### 3-4 Building for Everyone from the Start

I make a tool for my own shop, then hand it out to other shops too. It sounds simple when you say it, but to do it, the way you decide things before you start building has to change.

If I were building only for Tamuro, the quickest way would be to write Tamuro's business hours and Tamuro's name directly into the program. But then no other shop could use it. If you try to make it general-purpose later, you end up hunting down every hard-coded spot and fixing them one by one.

So the tools in the Agenda series are specified from the beginning on the premise that everyone can use them. I start from a problem at Tamuro, but at the requirements stage I separate two questions: "Is this only true of Tamuro, or is it true of every shop?" Don't put the shop's name on the sign. Let people choose the language. Make it pasteable into any website. I settled decisions like these while writing the requirements document for the Light Notebook.

This is another use for the requirements definition I relearned in Chapter 2. If you decide these things first, you can use the tool at Tamuro and hand it out to other shops as it is.

The problems in my shop are also the problems in other shops. I'm not the only owner who wants to tell customers that closing time is running late. An owner of an independent shop builds a tool out of their own problem, then hands it out to other shops. That is the idea behind the Agenda series.

### 3-5 The Democratization of Technology

The Agenda series now has more than 10 products. I build them and run them alone, while standing behind the bar.

A few years ago, this would have been unthinkable. To build one product, you needed someone to plan it, someone to design the screens, someone to write the code, someone to test it, and someone to operate it. Without a team and funding, you couldn't put a product into the world.

That is no longer true. The owner tells the AI the requirements, the AI writes the code, the AI tests it, and another AI audits it. What the owner does is decide what to build, judge whether the AI's results fit the shop's purpose, and do only the operations that humans alone can do.

This kind of change is generally called the "democratization of technology." The power to build is no longer the property of a few people or companies.

But let me be honest here. As I wrote in the Introduction, I worked in IT for about 16 years, mostly in system planning and as the coordinator between the people on site and the development vendors. I knew requirements definition, how to think about databases, and how to run tests, all from experience. So I won't claim that someone who has never written a line of code could do the same starting tomorrow.

Even so, a great deal has changed. I can now build, on my own and in the gaps between my main job, things at a scale that once took a team. And for people with no experience, the entrance has certainly gotten lower. AI will teach you if you ask about something you don't understand. It will give shape to what you tell it in words. What's missing is not technique but the ability to decide what to build and the words to tell the AI. Those are abilities that people who run shops use every day anyway.

### 3-6 The "Death of SaaS" Debate

Software that people use over the internet for a monthly fee, like the Agenda series, is called SaaS (Software as a Service). Accounting software, time and attendance management, reservation management. Restaurants today run on a lot of SaaS.

Will AI put an end to SaaS? In 2026, that debate flared up in a big way.

One trigger was a remark by Microsoft CEO Satya Nadella. On a podcast in December 2024, Nadella said that SaaS applications would collapse in the age of AI agents. The reasoning: once AI agents take over the decision-making part of business work, software built for people to operate through screens will no longer be needed.

Then in February 2026, Anthropic announced Claude Cowork (an AI tool that carries out business tasks autonomously), and shares of American software companies were sold off heavily. On Wall Street, the plunge came to be called the "SaaSpocalypse." What investors feared was that if AI agents do the work, the SaaS model of earning a fee per person (per-seat pricing) would fall apart.

There are counterarguments, too. Nvidia CEO Jensen Huang said that AI agents will not replace software but will use software on people's behalf, and called the selloff an overreaction. Quite a few others also see SaaS that absorbs AI as getting stronger, if anything.

Will SaaS really die? Here is what I think.

What dies is the middle layer of SaaS: the kind that charges a high monthly fee per seat and assumes people operate it through screens. If AI does the work in place of people, you don't need seats for each person. If no one is operating a screen, you don't need an elaborate screen.

What remains are tools that are cheap and do one thing reliably. And tools that are easy for AI to use.

This is exactly the three principles of the Agenda series. It runs automatically, it is left to the owner's AI (relying on others), and it does only one thing (single function). AgendaTurno leaves the work of building the shift schedule to the owner's AI, which is just the "AI uses the software" form Huang describes. Tamuro's reservation system opens a window through MCP to customers' AIs, and that is the same idea.

Of course, there may seem to be a contradiction here. I talk about the death of SaaS, yet the Agenda series is itself SaaS. But the Agenda series is a set of tools an owner built for their own shop and then made public at a low price. It is not a model that charges a high monthly fee per seat, and it does not assume that people sit glued to a screen every day. It is built from the start on the premise that AI will use it.

#### "The Death of SaaS" for Restaurants

This debate may sound like a story about investors and the IT industry. But for restaurants, the same thing is about to happen in a much more familiar form.

Many independent shops pay a monthly fee to gourmet sites and reservation sites, and on top of that pay a referral commission for every reservation. In exchange for bringing in customers, the site holds the connection to the customer, and it is not unusual for the shop to lack even the customer's contact information. If prices go up, the shop has no choice but to follow, and if the ranking system changes, the flow of customers changes.

As I wrote in Chapter 1, in 2026 the age began in which customers have their own AI search for shops. If the entrance shifts to AI, the whole arrangement of paying a site monthly fees and commissions to be placed high in its listings starts to wobble. If a shop opens a window to AI on its own, customers can reach it without going through the big sites. The reservation records and the relationship with the customer stay in the shop's hands.

If I put "the death of SaaS" in an independent shop's words, it is "the end of the era when paying got you listed." Tamuro opened its window through MCP, and keeps its reservations and CRM on its own specifications, as preparation for that.

Whether SaaS will die, no one knows yet. But the shape of the tools that will remain in the age of AI is gradually coming into view. That is what I think.

### 3-7 Monetization: Small, Many, Cheap

I build the Agenda series with the aim of making it stand as a business. The aim is to make it a second pillar of income, separate from the restaurant.

I set the prices small and low. Monthly fees start from a few hundred yen. The Time Clock, for example, is ¥500 (about $3.3) per month. I also mix in free tools, such as the Profit Planner, the Light Notebook and Recipe Costing. The free tools serve as the entrance by which people get to know the Agenda series. The Light Notebook uses neither a map API nor generative AI, so it costs almost nothing to run. That's why I can give it away free.

There is one account. With a shared account called AgendaID, you can use every tool in the series. You don't need to register again for each tool. Paid tools come with a three-month free period and can be started without registering a card. The free period is available only once per combination of shop and product. If you refer another shop, you get a bonus.

The reason I can keep prices low is in how I build. I build alone, I have AI do the building, and I reuse a shared foundation. The database cost is kept to about $35 per month for the whole series. If the cost to build and the cost to run are both small, a business can stand even on small sales.

Let me be honest. As I write this book, some shops have tried the tools, but there are almost no paid registrations. The system for building is in place, but the system for getting known is still ahead. This book is also meant to be a volume for that purpose, for getting known.

#### Building Something and Keeping People Using It Are Different Things

Let me be honest about one more thing. Being able to build a tool and having someone keep using it are separate matters.

Building has gotten faster thanks to AI. But getting people to keep using it takes other work. Answering questions about how to use it (the Support Guide exists for this). Sending a notice before the free period ends. Explaining the reason when raising a price. Properly deleting the data when someone asks to cancel. And above all, keeping it running without the owner touching it.

Of the three principles of the Agenda series, "automatic" is the principle for this "keep them using it." A tool that doesn't work unless the owner touches it every day will eventually be canceled. It isn't finished when it's built. It becomes a business only when it keeps being used. Adding, one by one, shops that keep using it: that is my job after publishing this book.

#### If You Want to Start at Your Own Shop

For those who read this book and want to try it at their own shop, there are three steps.

1. Open <https://bontallc.com/agenda?via=b2-en-kindle> and log in with a Google account (AgendaID will be created. No card registration is needed)
2. First, add one free notebook. I recommend the Light Notebook. You just paste the sign component into your website, and it works in 10 minutes. If you haven't opened yet, try the Profit Planner
3. If it seems to suit you, try the Time Clock free for three months. A notice arrives as the deadline approaches, so you won't be charged even if you leave it alone

If you have questions, ask through the Support Guide (AgendaQA). The AI answers operating questions instantly, and I read questions about specifications and bugs myself.

A restaurant's sales depend on the weather and the season. The number of seats and the business hours both have limits. Tool sales, on the other hand, have no limit on seats. Running a shop while handing out tools born from your own shop's problems, and having that slowly become income: I believe this can become another way for an independent shop to earn.

#### Staying a Small Company, Going Global

There is one more thing I decided about the Agenda series from the start. I would not build it in Japanese alone.

The Time Clock, the Profit Planner and the Support Guide can all be used in 20 languages. The screen text and the frequently asked questions, all of it. A tool built for a 19-seat bar in Tokyo works the same way in English, in Korean, in Vietnamese.

There are two reasons. One is that the problems of restaurants don't change when the country changes. You want to record when staff come and go. You want to know your profitability before opening. You want to tell customers that closing time has been extended. These are all problems that independent shops around the world share. The other is that the number of independent shops in Japan keeps falling. If I served only the Japanese-language market, tool sales would have a ceiling.

In the past, for a small company to sell products overseas, it needed local agents, translation firms and legal entities. Now AI helps with translation and proofreading. Shared payment systems work all over the world. For delivery you only need a server, and there is no stock or warehouse in each country. A tool made by one owner can be on the shelves of the world in 20 languages the day after it's made. In the past, only large companies could do that.

A very small company that does business with multiple countries from the start: such companies are sometimes called micro-multinationals (tiny multinational companies). Bonta LLC aims for exactly that, with one shop in Higashi-Nakano and one owner.

Of course, translating into 20 languages doesn't mean owners abroad will start using it right away. Some of the translations still await review by native speakers to sound natural. Even so, by removing the language barrier from the start, the ceiling on how far the tools can reach disappears, just as the ceiling on seats does.

How I am building that foundation is the story of Chapter 4.

![Figure 3-5: Language switching in the Support Guide. 20 languages are listed *(The screen is in Japanese.)*](images/fig3-5_qa-languages.png)

## Chapter 4: Technology - A System for Building Products Alone, Continuously

Key points of this chapter

- I turned the procedure for launching a new product into a document, in a form (a skill) that an AI can read and carry out. What humans do is only judgment and the operations that only humans can do
- The shared parts, such as login, billing, introduction pages and guides to other products, are built once and reused across all products. The database cost of that foundation is about $35 per month
- The system is still being grown. I keep adding to the procedure document the failures, such as a design being rejected five times in a row

(This is a chapter with a lot of technical terms. If you aren't interested in the technology, you can skip to Chapter 5 and the story still connects.)

### 4-1 ProductBootstrap: Handing the Launch Procedure Itself to the AI

Every time I built a product, I repeated the same preparation and the same mistakes. Create a repository (a storehouse for programs). Connect login. Decide the design colors. Set up the testing system. Prepare the production environment. I had surely done all of it for the previous product, but I'd forgotten the details and stumbled in the same places.

So I turned the procedure for launching a new product into a document. A form of it that the AI that writes code (Claude Code) can read and carry out is what I call a "skill." The name of this skill is ProductBootstrap. "Bootstrap" is a common term in the computer world for starting up on your own from a minimal mechanism, and I applied it to launching products.

I keep no template program. I copy the most recently completed product and start the new product from it. That way, the newest lessons are automatically passed on to the next product. There is no need to keep maintaining an old template, either.

#### The Flow of the Procedure

1. Hand over the requirements document. If the required fields (product name, what it does, who uses it, price, pricing unit, identifying color, location of the master design, and so on) are left blank, the AI does not start. The rule is that it does not ask the owner questions along the way. If everything isn't in place at the start, it doesn't begin
2. Decide the product's color. Each product in the Agenda series has one identifying color. The AI measures the colors of the existing products, proposes about four candidates that don't overlap, and the owner chooses
3. Fix the design. I have a design AI (Claude Design) create proposals for the screens. The AI runs its self-check up to three rounds, and only proposals that pass the check are shown to the owner
4. Leave the implementation to the AI through to the end. The AI builds and fixes on its own until it meets the set acceptance conditions (type checks, style checks, all tests green, passing every screen check, and database changes going through cleanly in the test environment)
5. The owner approves only when going to production. Everything up to the test environment proceeds unattended, and the owner judges only the production operation

I built the implementation stage so that it doesn't stop midway to wait for the owner's approval. In the early days, I proceeded by asking for approval at each stage, but nothing moved forward that way. When there are several AI work windows, each one stops waiting for approval, and the owner has to go around to every window making judgments. So I changed it: I hand over in advance the range that is already approved and the acceptance conditions that a machine can judge, and it stops only on failure.

The stopping conditions are also set. When the procedure document and the owner's ruling conflict. When an operation only a human can do becomes necessary. When it fails to progress on the same error three times in a row. When authentication lapses, permissions are insufficient, or an irreversible operation is needed. Otherwise, the AI proceeds on its own. The state of the work is recorded in a small file, so even if it crashes midway, it can resume from there.

#### Humans Do Only Two Things

I wrote this in the procedure document: the AI carries out every step. The owner may be asked for only the following two things.

- Judgment itself. Approving, ruling, deciding which of two options to take
- Operations only a human can do. Keys that can be issued only from an external service's admin screen, applications that involve identity verification, operations on a real device and visual judgment

If the AI hands anything else to the owner, that is a violation of the procedure document. In the procedure table, I added an "executor" column to each row, and any row whose owner entry can't state a reason gets switched to the AI's side.

I had a reason for making this rule. When I sorted out the remaining work for one product, the AI lined up "create the server project," "register the login destination," "enter the environment variables," and "build the test environment," all as the owner's tasks. Every one of them was an operation the AI could carry out itself. "Why am I the one doing this?" was my honest reaction at the time. The AI does things itself if you ask. But if you don't ask, it passes them to a person. That's why I had to write it into the procedure document.

I put every failure of the reservation system that I described in Chapter 2 into this procedure document's checklist. Put the tests in first. Don't keep production data in the development environment. Build the test environment first. The next product avoids the same pain from the start.

#### Still Growing

This procedure document is not a finished product. It is something I keep adding to every time something fails.

For example, there was a time when I had the design AI create the screen for one product five times in a row, and all five were rejected. That includes the rounds where I handed it the series-wide design rules (DESIGN.md).

At first, the AI diagnosed the cause as "the color scheme itself." I denied that. The actual causes were two. One was that colors with no definition in the rules were being used freely. The other was that three sections with different roles were stacked vertically with the same background color and the same margins, with no boundary between them. No rule had been violated, yet the roles had disappeared from the look.

So I added clauses to the design rules. Don't give things with different roles the same look. Don't separate them by color alone. The most important thing comes first in the line of sight. Only things that are truly equal may be lined up at the same weight. Don't make a layout that just stacks things vertically.

There was one more lesson from failure. If you convey the "default look to avoid" only as a list of prohibitions, the AI swings entirely to another default that isn't on the list. When I banned cards, shadows and rounded corners all at once, what came back was a newspaper-like screen made of nothing but rules and margins. Since then, I have the request materials written in three columns: "the pattern to avoid," "what I wanted to prohibit," and "what to do instead."

I also changed how I decide identifying colors partway through. Around when products exceeded eight, the band of dark colors was filled by existing products, and the ninth and later products could no longer get a dark color for lines and buttons without colliding with the existing ones. So I revised the rule: a product's identifying color is used only for light surface colors, and lines, rules, icons and main buttons are all unified in the series' shared ink color. It was a constraint that became clear only once the products multiplied.

Every time something fails, I fix the procedure document. The next product gets easier by that much. I believe growing the procedure document is the best investment for continuing to build products alone.

![Figure 4-2: The stages of the launch procedure, and who carries them out (the AI or the owner) *(The screen is in Japanese.)*](images/fig4-2_bootstrap-steps.png)

![Figure 4-3: The identifying colors of the Agenda series. One color per product, used only on surfaces *(The screen is in Japanese.)*](images/fig4-3_identity-colors.png)

### 4-2 AgendaHub: The Front Door

As products multiply, you end up building the same things again and again. Login, billing, introduction pages, guides to other products. To run this alone, you need to build the shared parts once and reuse them across all products.

AgendaHub is the place where those shared parts are gathered. I call it the "front door."

First, it is the entrance that routes from one address to every product. Under a single domain, bontallc.com, an entrance for each product is lined up: /agendatimbro, /agendaoro, /agendaluce. To customers it looks as if the products sit inside one site, but in fact a separate program runs behind each.

Next, it is where the product introduction pages are placed. There is one introduction page for the series, and within it a section for each product. Each section holds the product name and its nickname, the price, a problem stated in the owner's own words starting with "When you...," a description of what it can do, and a link to the detail page. When I release a new product, adding this section is included in the launch procedure.

And it is the home of the design rules and the launch procedures. The master of the identifying colors, the screen rules (DESIGN.md), the ProductBootstrap skill I described in 4-1, the skill that checks screens, and the skill that makes database changes safely. For every rule that spans the series, the actual content lives here, and each product reads it by reference.

![Figure 4-1: The structure of the Agenda series. From the front door (AgendaHub) to each notebook, and every notebook connects to one account (AgendaID) *(The screen is in Japanese.)*](images/fig4-1_series.png)

### 4-3 AgendaID: Shared Accounts and Billing

AgendaID is the series' shared system for accounts and billing.

An owner who logs in once with a Google account can use every product. There is no need to create an account for each product. I also plan to eventually carry language settings across products.

Billing is also a single system. Instead of building the connection to the payment service (Stripe) for each product, AgendaID takes it all on. There are four pricing categories: a light product at ¥300 (about $2) per month, a pay-as-you-use product, a one-time purchase product at ¥600 (about $4), and a free product. Paid products have a three-month free period without card registration, usable once per combination of shop and product. There is also a mechanism that adds three months of free period each to the referrer and the person referred.

Before the free period ends, notification emails arrive seven days and one day ahead. I first built these emails inside the Time Clock too, but as products multiplied I realized it was wasteful to give every product the same mechanism, so I consolidated it on the AgendaID side.

#### Cancellation and Deletion Under Shared Rules, Too

There is a part that is plain but important: cancellation and data deletion.

When a customer cancels, which data is deleted, and when? If you build it separately for each product, something will certainly be missed somewhere. What's more, the Agenda series includes products that handle especially sensitive data, such as the one that identifies regular customers by face recognition.

So I split the granularity of deletion into four levels and made it a rule shared across the series. They are canceling a product, deleting a shop, withdrawing an account (leaving the whole series), and a request for deletion from an individual staff member. The upper levels cascade to the lower ones, and each product registers its own data-deletion procedure with the shared system. The grace period for deletion is 30 days, and during that time it can be undone.

A time axis comes with this. Attendance records, for example, are required by law to be kept for five years. Even if a former staff member requests deletion, within the retention period the record must be kept, with names and the like anonymized, rather than physically erased. I needed to decide the line between "delete" and "keep" by checking it against the law.

#### A Test Login for Keeping the AI from Contaminating Production

I added one more mechanism to AgendaID, for the AI: a test login entrance.

To have the AI check that things work, the AI has to log in and operate the screens. But login is done with a Google account, so the AI can't log in by itself. And I can't hand the owner's account to the AI either. There is a danger that the AI's tests would contaminate production data.

So I built an entrance that issues synthetic accounts (personas) usable only in the test environment. It doesn't work in production. The test environment's database is a separate project from production and contains only synthetic data. The AI logs in through this entrance, operates the screens, and confirms that things work. The test accounts are rebuilt every day, and old ones are deleted.

With this, the AI can carry out even the final check on its own, in an environment built exactly like production, without touching production.

### 4-4 Common Navigation, and the Failure of the Word "Front Door"

So that users can get from any product to the others, I gave every product a shared navigation menu. It is the path that lets a bar owner using Time Clock ask a question in Support Guide, or go and look at the other notebooks.

There is a small failure story behind this shared navigation.

In the first version, I had placed a link that said "Back to the front door." That was because, internally, I called AgendaHub the "front door." But when I checked on a real device, something was off. Two links, "Back to the front door" and "See the Agenda series," jumped to the same place. On top of that, the support link sat above the everyday work menu, so the order of importance was backwards. And above all, the words "front door" mean nothing to an owner using the product for the first time. It was the maker's own internal language.

So I reset the principles. Order the items by how close they are to the user's purpose: everyday work at the very top, links leading outside at the very bottom. Even a link meant to win new users never goes above the work. The boundary must be explainable with a single line. Write the wording in the user's language, not internal language. Never put more than one link that jumps to the same place. I scrapped "Back to the front door" and merged everything into a single link, "See the other Agenda notebooks."

In Chapter 2, I wrote about learning the language of the UI. That was language for the owner to use when talking to the AI. This is the opposite: language the maker uses to talk to the user. In both cases, it was about fitting your words to the person you are speaking to.

![Figure 4-4: The shared navigation after the fix. Work is at the top, and the links leading outside are at the very bottom *(The screen is in Japanese.)*](images/fig4-4_series-nav.png)

### 4-5 The Foundation Costs $35 a Month

The database cost of the whole foundation described in this chapter is about $35 a month. The paid plan that includes the production project is $25, and the project for the test environment is $10.

This, too, was not the amount from the start. At one point I was paying $45 a month. The development database for a face recognition product was still being billed even though I wasn't using it. I moved it to the free tier and stopped it, deleted another project I wasn't using, and that is how it got to the current amount.

I also keep an eye on the cost of AI. The work of the AI that writes programs is billed by the amount of tokens (the unit of text the AI reads and writes). I avoid concentrating costs by having the work window stick to the role of coordinator and leaving the implementation itself to a different AI with a separate cost allowance. For the generative model in the chat window as well, I look at the price and choose what is necessary and sufficient. Even if a higher-tier model costs only $1 more per month, I choose by asking "is it enough?"

If you build small, even small sales can sustain you. The monetization story in Chapter 3 is supported by how small the cost of this foundation is.

### 4-6 The Coordinating AI, and the Person Who Makes the Call

Finally, let me describe the shape of my working day.

I keep several AI work windows open at the same time. There is a window for the reservation system, a window for each product, and a coordinator window that sends instructions to them and gathers the results. I named the coordinator window AgendaRegia (the coordinating notebook).

The ones who make the rulings, that is, decide "which way to go," are me and the AI on the chat side. The chat-side AI finds gaps and contradictions in the specifications ahead of time, attaches a default ruling to each, and proposes them all at once. I read them and decide. What is decided is gathered into an instruction sheet called a Goal and pasted into the work window. It includes advance approvals and pass conditions that a machine can judge. The work window reads it and carries on to the end, stopping only when something fails.

I also have the instruction sheet include an estimate of when the work will be done. I fit this work in between the bar's opening hours, so if I don't know how long something will take, I can't plan my day.

The owner's role is not reading but deciding. I don't need to read all 1,775 conversation logs. I answer questions about facts of the bar. I rule on things that only the bar's policy can decide. After something goes live, I touch it five or six times myself to check whether anything feels off. That's all.

Before arriving at this form, I redid work many times. The AI added features on its own and the screens became unstable. The work grew without limit from a single instruction. Waiting for approval at every stage meant nothing moved forward. Each time, I added one rule, and that is how it reached its current form. This, too, is still growing.

#### What You Can Take Away from This Chapter

- For repeated work, turn the procedure itself into a document and hand it to the AI. If you fix the manual each time it fails, the next time gets easier
- Build the common parts (login, billing, navigation) just once and reuse them across all products. If the foundation is small, even small sales can sustain you
- Humans do only the judgment and the operations only humans can do. If the AI hands you anything else, add it to the manual

The continuation of this chapter (the next notebooks I build, and the lessons I added to the manual) is on note and X. note <https://note.com/bontallc> / X <https://x.com/tamuro_hnakano>

## Chapter 5: A Small Bar's Future

### 5-1 From Zatta Gohan to Tamuro

I entered the food and drink business when I was 39.

The trigger was a neighborhood bar called Zatta. Once a month, sometimes every other week, they let me serve meals there. I had taught myself to cook for a long time, but now I had a place where people ate my food and were happy. That was my original experience.

In 2014, I opened a restaurant called Zatta Gohan in Arai-Yakushi. It was a small place that served set meals. I ran it for seven years.

In Arai-Yakushi, though, I felt a limit on the number of customers. Then I found a property in Higashi-Nakano. It takes less than a minute to walk from the east exit of the station. Even on a rainy day, you can get there without getting very wet.

In November 2018, I opened Tamuro there. "Tamuro" means a place where people gather. It has 11 counter seats and 8 tatami seats, 19 in all. For three years I ran two places in parallel, Arai-Yakushi and Higashi-Nakano. During the COVID period, keeping both became difficult, so I closed the Arai-Yakushi shop and was left with Tamuro alone.

#### The Curation Bar

Tamuro calls itself a "curation bar."

Curation means having a discerning eye. Before I am a cook, I want to be a curator. The food, the drinks, the atmosphere of the bar: I make everything by selecting with a discerning eye. That is Tamuro.

I often travel to eat, both abroad and in Japan. Vietnam, Cambodia, Italy, Shanghai, Beijing, Mexico. Eating my way around is a pleasure, and at the same time it is a way of finding what to serve at Tamuro. I recreate expensive ingredients with ingredients within reach. For example, if you dry egg yolk and shave it, you get a flavor close to bottarga. I think of this kind of substitution (localization) as my role.

I studied cooking again during the COVID period. I took a French cooking course of eight sessions in total, and I also attended a course in Japanese cuisine. How to handle umami, and how to cook with heat. What I learned there is the foundation of my cooking today.

Tamuro's menu is built from four appetizers and one main. I give it a range of ingredients so that customers who live alone can get plenty of vegetables. I put it together so that cooking methods (fried, vinegared, simmered, grilled) and flavors (sweet, spicy, sour) don't overlap. The most popular dish is tonteki, pork steak. It has a slightly sweet sauce made with Kyushu soy sauce, with plenty of garlic.

#### A Place Where People Gather

About half of Tamuro's customers come alone. They are mainly in their 30s to 50s, and many are neighbors from Higashi-Nakano, but people also come from around Akabane, Shinjuku, Nishi-Ogikubo, Ogikubo and Eifukucho. 

The bar's distinguishing feature is how much the customers talk with each other. I built the counter so it is easy to talk to the person next to you, and I or the staff decide seating by judging who will get along. Customers who came alone sometimes come back together later. As the name says, it has become a place where people gather. I post what the bar's days look like on [Instagram](https://www.instagram.com/tamuro.higashinakano/).

In the course dinner held about once a month, I serve seven to eight dishes over two to three hours, together with wine pairings. Each month the theme changes: Italian, French, Japanese. The cooking classes are three-hour workshops, and after cooking, everyone toasts, eats and goes home. There is the aperitivo, serving wine and small plates in the early evening before opening. There is a barbecue about twice a year. There is a year-end party once a year. And there is the yukata festival I wrote about in Chapter 1.

The reservation system I wrote about in Chapter 1, the chat window, and MCP are all tools to bring people to this bar. AI is a means of gathering people, not the goal.

### 5-2 Quatre Épices' Hamburger Curry

Tamuro is a night-time bar. During the day, the space is empty.

Using that time, I started Quatre Épices in January 2024. It is a hamburger curry shop that operates only at lunchtime in the same place, and the staff run it.

Quatre Épices means "four spices" in French. True to the name, rather than layering on lots of spices, we choose and narrow them down to make the outline of the flavor clear. The curry uses no flour; it is finished with the natural thickness of the vegetables and meat themselves. Satisfaction when you finish eating, and no heaviness in the stomach. And harmony with the hamburger. I designed it on those three premises.

We are particular about how the hamburger is cooked. We set the blend so that it comes out crisp outside and fluffy inside, and we cook to suit that blend. The way of cooking with heat that I learned at night at Tamuro serves the daytime plate too.

Prices, business days and hours can change, so please check Tamuro's Instagram (https://www.instagram.com/tamuro.higashinakano/) for the latest information.

Quatre Épices also runs a children's cafeteria in the same place. It is an activity that uses the existing bar's facilities and purchasing to serve meals to children in the neighborhood. Through that connection, we also built a relationship with the local community center. We sometimes serve curry and sandwiches at local sports events, community center events and Bon dance festivals.

To be honest, using the daytime hours has not all gone well. I created days for daytime drinking and rented the space to other people, but customers did not come as I hoped. The bar's appeal comes across differently when the owner is there at night and when only the daytime staff are there. Growing the daytime shop with an appeal different from the night shop's is still an unfinished task.

### 5-3 Bonta LLC: Two Pillars

The small company that runs Tamuro and Quatre Épices is Bonta LLC. I am its managing member.

The company has two pillars. One is food and drink: Tamuro and Quatre Épices. The other is IT: development of the Agenda series, and consulting.

Food and drink and tools differ in how they earn money. Supporting the company with two pillars of different natures is the form I have in mind.

And the two pillars supply each other with materials. Trouble at the bar becomes the seed of a tool. What I learn from building tools comes back into running the bar. The Light Notebook was born from closing times running late, and the extended-hours records from the Light Notebook become the basis for profit estimates and shifts. The "questions we could not answer" that pile up in the chat window improve the bar's guidance. This cycle is the reason I can manage both the bar and development on my own.

I am not thinking of making the company bigger. Small, many, and cheap. That is the shape of this company.

### 5-4 Writing as Raku Bonta

When I write and publish, I use the pen name "Raku Bonta." I wrote this book under that name too.

My previous book, *The AI Deputy Manager*, was a book about generative AI. It ranked number one in Amazon's time management category and was read by many people. This book is its sequel.

Besides books, I also write on note. I write about the bar's efforts with AI, what I found on a training trip, the progress of publishing my books, and the Agenda series. You can follow the continuation I couldn't fit in this book on note (https://note.com/bontallc).

For me, writing is also a way to put both the bar and development into words and check them. As I wrote in Chapter 1, the first knowledge of the chat window "T-AI-MURO" was built from words I had been leaving on X. What I had written down became material for the AI. From now on, too, what I write will return to both the bar and the AI.

There is one more thing I have decided about writing. I don't announce unfinished things with "coming soon." I finish it, make an introduction page, and only then put it out. I believe keeping to that order is what earns a small company trust.

### 5-5 The Future of the Independent Shop

Finally, I'll gather what I've written in this book into a single picture.

![Figure 5-1: The big picture of what this book has described. A small bar opens its own window (the first story), and turns its troubles into tools to hand to other bars (the second story) *(The screen is in Japanese.)*](images/fig5-1_summary.png)

Customers will come to have their own AI find a bar and make the reservation. In August 2026, it became possible to book restaurants from ChatGPT through a major reservation service. The entrance is shifting from search and food review sites to each person's own AI.

At that point, a bar not listed on the major reservation service is invisible to the AI. But even if you are not on the major service, there is a path for a bar to connect directly to the AI. Tamuro chose that path by opening a window called MCP. A small bar opening its own window by itself. That is the first story of this book.

Bar owners will be able to turn their own troubles into tools and hand them out to other bars. The Light Notebook was born from Tamuro's trouble of wanting to tell people that closing time would run late, and it can be used at any bar. The power to build is becoming something that is no longer only for certain people or companies. A small bar owner moves from the side that uses tools to the side that builds and distributes them. That is the second story of this book.

What these two have in common is that the smaller the bar, the sharper it can be.

Large chains generalize their systems so that every outlet delivers the same quality. Tamuro is the opposite. Solo customers make up half, nearly 90% of reservations are made the same day, and customers talk to each other. To fit that character of Tamuro, I have built the reservation system, the discounts and the chat window in detail. Because it doesn't generalize, it is sharp. Because it is sharp, it becomes a reason for customers to choose it.

And the sharper the bar, the more seeds of tools it finds. The more you face the bar's character, the more specific your troubles become. Specific troubles become specific tools. Specific tools help other bars that have the same trouble.

AI has made it possible for a single owner to do both. Sharpening the bar, and handing out tools. Once, you had to choose one or the other. Now you can do both.

Of course, it's still a work in progress. The pass rate of the chat window is still being raised. The manual gets added to with every failure. How to grow the daytime shop remains a challenge. People who book through AI are still not many.

Even so, I believe the future of the small bar is bright. Being small is not a weakness. Because we are small, we can test fast, drop fast and fix fast. Because we are small, we can be sharp. And the troubles of a sharp bar become tools and pass on to other small bars.

I wrote this book from a 19-seat bar in Higashi-Nakano.

## Afterword

Thank you for reading this far.

What I wrote in this book is a record as of October 2026. AI tools change their shape in a matter of months. Some of the mechanisms I described may already have taken a different form by the time this is published. Even so, I wrote it down, believing that a record of what a small bar built with AI and how, where it failed and what it learned, should stay useful for a while.

The Agenda series: <https://bontallc.com/agenda?via=b2-en-kindle>

Follow my activities: note <https://note.com/bontallc> / X <https://x.com/tamuro_hnakano>

If you are ever in Higashi-Nakano, drop by Tamuro. You can reserve through the reservation site, through the chat window "T-AI-MURO" on the site, and of course through your own AI.

Tamuro's reservation site: <https://tamuroreservation.vercel.app/?src=b2-en-kindle>

Tamuro's Instagram: <https://www.instagram.com/tamuro.higashinakano/>

For those who want to try booking from AI. The connection address for Tamuro's MCP server is the following URL.

<https://tamuroreservation.vercel.app/api/mcp>

In the settings of your AI (such as Claude or ChatGPT), open the screen for adding external tools (connectors, MCP servers) and register this URL. How to register varies by AI and over time, so the safest approach is to look up "MCP" or "connector" in each AI's help. Depending on the plan you have, you may not be able to connect an MCP server of your own choosing. Once registered, ask your AI, "Is Tamuro open tonight?" It will check the open slots and prices and guide you to the reservation page. The confirm button is pressed by you.

For those who came after reading the book. When you reserve, please enter the coupon code "BOOK." We will serve you one drink on the house for your first round. If you came without a reservation, just say "I saw the book" when you place your first order. We will serve you the same drink. It is a small device that lets me count how many people came from the book.

You can come in without a reservation. Even alone, you won't stand out. You may even end up chatting happily with the person next to you.

I'm waiting for you at a place where people gather.

Raku Bonta

### References

- OpenAI Help Center, "ChatGPT — Release Notes," August 10, 2026, "Restaurant reservations in ChatGPT" <https://help.openai.com/en/articles/6825453-chatgpt-release-notes>
- Alpaca, "Alpaca MCP Server" (an example of an MCP server in the US that lets AI place orders for stocks and other securities) <https://docs.alpaca.markets/docs/alpaca-mcp-server>
- The "death of SaaS" debate: Satya Nadella's remarks on the BG2 podcast (December 2024), the sharp drop in software stocks in February 2026 and what it was called, and Jensen Huang's rebuttal were drawn from the following reports and commentaries. <https://www.longangle.com/alts-education/software-ai>  /  <https://www.fastcompany.com/91504460/everything-youve-heard-about-the-saaspocalypse-is-wrong>  /  <https://en.thairath.co.th/money/tech_innovation/tech_companies/2916811>

## Colophon

- Title: Built for Our Bar
- Subtitle: How the Owner of a 19-Seat Bar Built Everything from Reservations to Tools with AI
- Author: Raku Bonta
- Publisher: Bonta LLC
- Edition: English edition, first edition (translated from the Japanese original)
- Published: 2026-10-30
- Language: English
- Translation: translated from the Japanese by AI and reviewed by AI. Short notes on Japanese places, systems and customs were added by the translator. Yen amounts are followed by approximate US dollar figures at ¥150 to the dollar (as of 2026-10-29).
- Free to share

The Agenda series: <https://bontallc.com/agenda?via=b2-en-kindle>

Tamuro's Instagram: <https://www.instagram.com/tamuro.higashinakano/>

Tamuro's reservation site: <https://tamuroreservation.vercel.app/?src=b2-en-kindle>

note: <https://note.com/bontallc>

X: <https://x.com/tamuro_hnakano>
