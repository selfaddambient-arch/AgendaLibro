# うちの店は、うちの仕様で

19席のバー店主が、AIで予約システムから道具まで自分で作った記録

Raku Bonta

the Agenda series: https://bontallc.com/agenda?via=b2-en-{{FMT}}

Tamuro's Instagram: https://www.instagram.com/tamuro.higashinakano/

Tamuro's reservation site: https://tamuroreservation.vercel.app/?src=b2-en-{{FMT}}

## Introduction

This book is a plain record of how the owner of a 19-seat bar in Higashi-Nakano ⟦a residential neighborhood in western Tokyo, just west of Shinjuku⟧, Tokyo, runs the shop with the help of AI.

The bar is called "Tamuro." The name means a place where people gather. It opened in November 2018, a small place with 11 counter seats and 8 tatami-room seats. In the daytime, in the same space, a staff member runs a hamburger-curry restaurant called "Quatre Épices."

In my previous book, *Running the Shop Alone, and AI Showed Up Beside Me*, I wrote about generative AI itself. In the year or so since, AI has changed from a tool that answers questions into a tool that gets work done for you. Give it an instruction, and it writes the program, tests it, fixes its mistakes and finishes the job. We call this kind of AI agentic AI.

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

I worked as a systems engineer for about 16 years, and then entered the food and drink business. So this is not a story of someone who had never written a line of code building everything with AI alone. I want to be honest about that.

Even so, I can now build and run, on my own while working the floor, something of a scale that once required a team and funding. A few years ago, that would have been unthinkable. I want to describe the reality of that change as concretely as I can.

### How This Book Was Made

I made this book with AI too. Starting from the records I have kept during my daily development work, the AI wrote the drafts, and I read, revised and made the decisions. I also had the AI take the screenshots used as illustrations.

I have read through everything, but text written by AI can have things mixed in that are not true. As I say in the main text, AI says "it's done," and checking that is a human's job. There may be mistakes in this book that I overlooked.

Also, the specifications of AI tools and services change within a few months. The steps, prices and each company's support status described in this book are as of October 2026. When you try things yourself, please check the official information at that time.

If you spot a mistake, I would be glad if you told me on note or X. I will correct things as I learn of them.

### The Three Exits of This Book

This book is free to read as a PDF, on note, and on Google Play. (Only on Kindle, the store's rules require a minimum price.) In return, I have prepared three places you can go after you finish reading. If even one of them is useful to you, writing this book was worth it.

1. Try it in your own shop. You can start the Agenda series with the free notebook. https://bontallc.com/agenda?via=b2-en-{{FMT}}
2. Follow what I do. I write about the next tools I build, and about daily life at the shop, on note and X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
3. If you are ever in Tokyo, visit Tamuro. One minute from the east exit of Higashi-Nakano Station. You can come in without a reservation. Reservation site https://tamuroreservation.vercel.app/?src=b2-en-{{FMT}}

## Chapter 1: A Shop That AI Books

### 1-1　"Is Anywhere Open Tonight?" You Ask the AI

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

【Figure 1-1】The screen after connecting from ChatGPT to Tamuro's MCP server (October 10, 2026). It reads the shop's information and answers that it can handle open times, courses, prices and guiding to the reservation page ⟦The screen is in Japanese.⟧

### 1-2　The Starting Point: Just Taking Reservations

[Tamuro's reservation site](https://tamuroreservation.vercel.app/?src=b2-en-{{FMT}}) was very simple at first. Choose a date, time and party size, enter a name and contact details, and send. A notification reaches the shop. That's all.

I built the first foundation with Google's AI development tool (Antigravity). I told the AI about each feature I thought of, and when something worked, I moved on to the next. It's what is called vibe coding (telling the AI whatever comes to mind and having it build by feel).

For me at the time, it was one surprise after another. Describe the layout of a screen in words, and it takes shape in minutes. Say you want a calendar, and a calendar appears. In the gaps while running the shop, one reservation site came together.

Tamuro is a place you can enter without a reservation. In fact, most reservations are made the same day, and many customers just walk in. Even so, I built a reservation system because I wanted a way to connect with customers before they visit. Once someone reserves, their name and contact details remain. Once their contact details remain, I can invite them to come again.

A reservation system is not just a front desk. It becomes the entrance to a relationship with the customer. This idea led later to the discount system and the system for nurturing regulars.

But for a foundation built on instinct, I ended up paying a big price later. I will write about that in Chapter 2.

### 1-3　Building a Price Increase and Discounts at the Same Time

For a restaurant or bar, a price increase is a decision you can't avoid. Ingredients, utilities and labor all keep getting more expensive. Tamuro raised prices too. I raised each course by about ¥400–¥500.

The increase was large, so it was obvious that if I put it out as it was, regulars would drift away. So at the same time as the price increase, I decided to build a discount system into the reservation system. It doesn't just make things cheaper. It rewards, with discounts, the customers who act in ways that are good for the shop.

The first is the group discount. The more people in the party, the lower the price per person. About half of Tamuro's customers come alone, but if they come in groups, the shop's sales grow a great deal. Even after subtracting the discount, the shop comes out ahead. For customers, too, it is a reason to invite friends. In fact, the number of customers coming in groups using the reservation site's party-size discount has grown.

The second is the early-bird discount. Reserve up to one week ahead and you get 2% off; up to two weeks ahead, 4% off. Most Tamuro reservations are made the same day, so I can't read what's coming. The early-bird discount is a mechanism for locking in future sales. On rainy days and cold days, if reservations are already in, the shop can prepare with peace of mind.

Third, I also built a group-buying mechanism. If a set number of people gathered at a set date and time, a set-meal course would be offered at a discounted price. It was supposed to be a mechanism with the Tamuro spirit, where strangers gather at the same time.

But the group-buying plan was not used at all. Zero results. In August 2026 I stopped this plan and decided not to use it again.

Throwing away something you made feels wasteful. But if you build with AI, the cost and time of building are small. Build small, try it, and if it doesn't work, throw it away. I believe this speed is the greatest advantage of running a shop with AI.

There is one more trick in the pricing. Among the plans, I deliberately place an expensive premium plan. It's fine if almost nobody chooses the premium plan. With a pricey plan beside it, the standard looks affordable. It plays the role of what is called an anchor (a reference point for comparison).

【Figure 1-7】The more people, the lower the price per person (comparison of 1, 4 and 6 guests)

### 1-4　A System for Nurturing Regulars

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

【Figure 1-8】Plans that only first-timers and people who haven't visited in over a year can choose ⟦The screen is in Japanese.⟧

【Figure 1-9】The stamp card on My Page (synthetic data) ⟦The screen is in Japanese.⟧

【Figure 1-5】Reservation confirmation email. One "Today's Topic" is included (synthetic data) ⟦The screen is in Japanese.⟧

### 1-5　By the Numbers: About 88% of Reservations Are Same-Day

As I kept adding mechanisms, I noticed something. I couldn't tell which of them were working.

So I counted the reservation data. Of the 244 reservations in the most recent 90 days, 215 were same-day reservations. That is 88.1%. The average is 2.71 reservations per day.

Tamuro was not a place people reserve for, but a place people come to on impulse. It only became clear once I put it into numbers.

Two things became visible from these numbers.

One is how to build the reservation form. If most reservations are for the same day, it is more convenient if the nearest open slot today is already selected when the reservation screen opens. On the other hand, some people who want to book a later date will carelessly send it as today. So I made today stand out on the calendar, and on the confirmation screen I show the date and time large with "Today." I kept the convenience of choosing the same day, and made mistakes easy to notice.

The other is the meaning of the early-bird discount. Many same-day reservations means we can't read future sales. Bad weather alone is enough to lower foot traffic. To increase advance reservations even a little, more people need to use the early-bird discount. This awareness later led to the story of building an AI that posts on the owner's behalf.

To look at numbers, you need a system for counting. The reservation site had no access analytics at all. I couldn't tell how many people came to the reservation page, how many quit partway, and how many finished. So I added a system that counts three stages: arrived at the page, decided on the details, finished the reservation. It doesn't record who came, only the stage and the time.

Later still, I also built a system that emails a weekly report summarizing the reservation numbers. I will describe how that came about in 1-7.

【Figure 1-3a】Today stands out on the calendar ⟦The screen is in Japanese.⟧

【Figure 1-3b】On the confirmation screen, the date and time appear large as "Today" ⟦The screen is in Japanese.⟧

### 1-6　Too Many Plans to Choose From

Once the discount system was in place, I wanted next to increase the hours and plans that sell.

The 6 p.m. hour wasn't filling up, so I created a happy hour until 7 p.m. For people who come after eating, I created a drink-only plan with no meal. The course meal and cooking class, once held monthly, I turned into on-demand events that open when someone signs up, taken through the reservation site. To sell the time before opening on weekends, from 3:30 p.m., I created a party plan for groups of six or more.

Each one has a reason. The party plan, for example: if I made it look like a bargain on price, it would only draw in customers who had been choosing the standard plan, and sales would drop. So I placed the differentiation not on price but on the pre-opening hours, which had never brought in any sales. The happy hour discount makes no profit if combined with other discounts, so I decided it can't be combined.

And so the plans multiplied. Standard, Premium, Nice to Meet You, Welcome Back, Happy Hour, Drink Only, Course Meal, Cooking Class, Party. Each has conditions on party size, some accept discounts and some don't, and there are time restrictions.

One day I opened the reservation form and realized: customers can't choose with this.

I, the builder, understand every difference. But could someone opening the reservation site for the first time compare nine plans and their discount conditions and pick the one that suits them? If they can't, they give up partway through booking. The plans I worked to add could end up reducing reservations.

I could have tidied up. But every plan has a time I want to sell and a customer I want to see. I didn't want to cut any.

So I thought of a system where the customer consults the AI and decides on a plan. Tell it the party size, the date and time you'd like to come, and how you want to enjoy the evening, and the AI gives the suitable plan and price and takes you straight to booking. The shop shoulders the complexity of the plans. What remains for the customer is just a conversation.

This system is the "T-AI-MURO" I write about in 1-8. Before that, there is one more thing I noticed during this period.

【Figure 1-2】Plan selection on the reservation form. This many tabs are lined up ⟦The screen is in Japanese.⟧

### 1-7　"Does This Actually Bring in Customers?"

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

【Figure 1-6】The weekly customer-acquisition report that arrives each week (synthetic data) ⟦The screen is in Japanese.⟧