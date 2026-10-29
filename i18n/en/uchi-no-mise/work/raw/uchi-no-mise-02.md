### 1-8　A Window That Talks with the Shop: "T-AI-MURO"

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

#### The scene where "budget ¥5,000" failed

I had attached an AI verdict to the AI tests too. A different AI reads the conversation log and decides pass or fail.

Among them was a scenario with a customer whose "budget is ¥5,000." The AI's verdict was a pass. T-AI-MURO had politely presented plans within the budget.

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

> Try it: Open Tamuro's reservation site (https://tamuroreservation.vercel.app/?src=b2-en-{{FMT}}) and ask T-AI-MURO "alone tonight." The conversation takes you through to today's availability and prices.

【Figure 1-4】The T-AI-MURO conversation screen. The conversation moves forward just by tapping choices ⟦The screen is in Japanese.⟧

【Figure 1-10】Questions it couldn't answer pile up in the admin screen (synthetic data) ⟦The screen is in Japanese.⟧

### 1-9　And Then, from the Customer's AI

By building T-AI-MURO, Tamuro's reservation site gained the ability to "answer questions about the shop in conversation, show prices and open slots, and guide people through to a reservation."

What I thought of next was making it possible to do the same thing from the customers' own AI.

T-AI-MURO can only talk with people who come to Tamuro's reservation site. But many people consult the AI they use every day first. If that AI doesn't know about Tamuro, Tamuro won't even make the list of candidates. Instead of waiting for customers to come to Tamuro's site, open Tamuro's window on the customer's AI side. That is the MCP server.

To be honest, I hesitated at first about building this. At this point, not many people book restaurants from their own AI. Judging that I couldn't expect a direct increase in reservations, I once lowered its priority and put it on hold.

I decided to build it anyway because I thought it was only a matter of time before the entrance changes. As I wrote at the start, in August 2026 it became possible to make reservations from ChatGPT through a major reservation service. Sooner or later, having AI find a restaurant for you will be the norm. When that happens, small shops that aren't listed on the big services will drop out of the AI's sight. So, open the window before the entrance changes.

What I decided for the first version was very narrow. It only needed to do the same as the conversation window on the reservation site (T-AI-MURO). All it can do is read the shop's information, open slots, and prices, and hand over the URL of a reservation page with the conditions filled in. Confirming the reservation is done by the customer themselves on Tamuro's page. The customer's AI doesn't confirm a reservation on its own. The final push is made by a person.

Let's go back to the opening scene.

On a Friday evening, a customer asks their own AI, "Is there a place in Higashi-Nakano ⟦a residential neighborhood in western Tokyo, just west of Shinjuku⟧ where I can drink alone tonight?" The AI queries Tamuro's window. Tamuro's reservation system returns tonight's open slots, plus the plan and price that suit a solo customer. The AI tells the customer, and offers a Tamuro reservation page with the date, time, and number of people filled in.

Everything I've written about in this chapter supports this series of steps. The discount system built along with the price increase. The system that nurtures regulars. The data that showed most reservations are made on the day. The shop knowledge grown by answering 11 questions one line each. The principle of putting the customer's wishes ahead of the shop's recommendations.

A shop that gets booked through AI wasn't built overnight. It stands on the accumulation of small systems added one at a time, tested, discarded, and fixed.

> Try it: Register Tamuro's MCP server (https://tamuroreservation.vercel.app/api/mcp) with your own AI and ask, "Is Tamuro open tonight?" How to register is written in the Afterword.

### 1-10　What We Built, and What Worked

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

### 2-1　How the MCP Server Works

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

【Figure 2-1】From the customer's AI to Tamuro's reservation page. The customer presses the confirm button

### 2-2　How the Conversation Window "T-AI-MURO" Works

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

AI tests cost money. The first 36-scenario test cost about ¥426. Most of it went to the "thinking effort" of the customer-playing AI, and when I turned that off, 3 scenarios cost about ¥6.

But then one day, partway through a test, the AI usage balance ran out and everything stopped. In a single day I had used about 35 million tokens (the unit of text an AI reads and writes). The cause was running the 221-scenario test over and over, and running scenarios tied directly to sales four times each.

What was frightening was that the test and production used the same wallet. When the balance runs out, even the production conversation window stops. On another day, this time I hit a monthly cap I had set myself, and the production conversation window and the AI that creates conversation topics for customers in the shop stopped at the same time.

The real danger of a testing budget was not the bill, but that production was using the same wallet.

From there the rules changed. Do the checks that cost nothing (program tests and automatic screen checks) first. Limit the AI-calling tests to those related to what was fixed. Run the all-cases test only once, before going to production. Write the estimated cost and a cap in the instructions, and stop if it looks likely to be reached. To keep funds for production, stop testing when the organization-wide usage gets close to the cap.

There was also a lesson in how costs swell. Once, the judging AI's cost came to 2.6 times the estimate. The cause was that the long preamble handed to the judge every time (the shop's knowledge and rules) wasn't being reused, so a rewrite charge was incurred each time. When I fixed it to write the preamble in once and reuse it, the cost per conversation dropped to about a third. AI cost swells not with how many times you call it, but with how many times you rewrite the same preamble.

The same 221-scenario full test came down from about ¥1,040 to about ¥400 through repeated improvements. I replaced the customer-playing AI with a fixed script, and split the information handed to the AI into a "core sent every time" and "sections read only when needed."

Because of budget constraints, the design changed toward increasing the parts that can be checked at zero cost, that is, the parts decided by the program. As a result, accuracy rose too. Money changes design.

【Figure 2-2】Results of the AI tests. The pass rate and a breakdown of the causes of errors