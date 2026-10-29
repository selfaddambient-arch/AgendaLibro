### 2-3　Having AI Audit What I Built

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

【Figure 2-3】The rules when it could be read from outside, and the rules after the fix (excerpt) ⟦The screen is in Japanese.⟧

### 2-4　Building by Feel Multiplies Contradictions

The more features I added, the more parts there were that clashed with what I had decided earlier.

The typical case was the discount calculation. In the reservation form, the confirmation screen, the email, and the admin screen, the discount calculation was written separately in each place. If I changed a discount rule in one place, another place kept calculating with the old rule. For the same reservation, the screen and the email could show different amounts.

Later, I gathered the price calculation into a single file. The reservation form, the chat window, and the MCP server all produce prices from there.

The rules for stacking discounts also changed along the way. As I wrote in Chapter 1, happy hour was originally going to be combinable with other discounts, but I found it would not turn a profit and changed it to non-combinable. Every time a rule changed, a person had to remember where to fix things. That was the weakness of a system built by feel.

There was also a mismatch between the test environment and production. While testing the chat window, a question, "Wasn't there something like 10% off?", revealed that the discount rules in the test environment had drifted from production. If the values in the test environment differ from production, you can pass the tests and still be wrong in production. What I decided then was the principle that "production is correct." Since then, before every test run, I copy the production settings into the test environment and confirm that the mismatch is zero before running.

AI builds what it is told. But it does not notice contradictions with earlier decisions. What prevents contradictions is not the AI. It is deciding things beforehand.

### 2-5　Relearning Requirements Definition

After reflecting on the reservation system I built by feel, I relearned requirements definition. Requirements definition means deciding, before you build, what you will build, what you will not build, and who will use it and how, and writing it down in a document.

It was something I did as a matter of course back when I was a systems engineer. But once I could build with AI, I had skipped it without noticing. Tell it an idea and something working appears in minutes. In that speed, I had cut the effort of deciding.

My way of building now has three stages.

1. First, decide the requirements in detail. What to build, what not to build, who will use it. The behavior of each screen. How to handle exceptions (errors, double presses, expiry). Rules that easily end up contradicting each other later, like prices and discounts, I decide in particular detail. I do this work too in dialogue with the chat AI. I have the AI find holes and contradictions ahead of time, and the owner decides.
2. Write what was decided as a "requirements document." Not spoken or on-the-spot instructions, but gathered into one document. This becomes the only standard for checking later what is correct.
3. Hand the whole document to the AI and have it implement. I give the whole document to the AI that writes the program (Claude Code), together with the conditions for passing (all tests pass, check in the test environment before production, and so on). The AI builds on its own until it meets the conditions, and checks on its own. The owner looks only when it stops partway and at the final check.

For example, the requirements document for the chat window "T-AI-MURO" was rewritten from the first version through the third. In the second version I decided "do not let the AI calculate prices," "put the shop's knowledge and the price calculation into one window," and "keep the form too, for people who do not want to reserve by chat." In the third version I decided "where to keep the master copy of the shop's knowledge," "this window alone shows open slots," "make the first exchange a four-choice question," and "do not save conversation logs; store only the questions that could not be answered." Because the decisions remain in a document, I can trace later why things are the way they are.

With this way of building, even when I add features, I can notice contradictions right away by checking against the document. Precisely in an age when AI does the building, the "power to decide" before building is needed. That was the biggest lesson I learned from the reservation system.

I also built a mechanism that puts the procedure itself into a document and hands it to the AI, so this way of building can be run the same way each time I launch a new product. I will write about that in Chapter 4.

【Figure 2-4】Table of contents of the T-AI-MURO requirements document (version 3) ⟦The screen is in Japanese.⟧

### 2-6　Learning the Language of UI

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

The continuation of this chapter (newly found holes and the steps I took to fix them) is on note and X. note https://note.com/bontallc／X https://x.com/tamuro\_hnakano

## Chapter 3: Distributing My Shop's Tools to Other Shops

### 3-1　The Small Green Sign on the Reservation Page

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

【Figure 3-1a】The Light Notebook sign on top of the reservation page (open) ⟦The screen is in Japanese.⟧

【Figure 3-1b】A touch of vermilion appears during an extension ⟦The screen is in Japanese.⟧

【Figure 3-6a】The owner's screen. To extend, press the button once ⟦The screen is in Japanese.⟧

【Figure 3-6b】Right after pressing extend. The closing time moves back 30 minutes ⟦The screen is in Japanese.⟧

【Figure 3-6c】The public page customers see (during an extension) ⟦The screen is in Japanese.⟧

### 3-2　It Began with the Black Leather Notebook

The Agenda series was not planned as a series. It began with a single system, one that has not even been released yet.

What I first set out to build was a mechanism that recognizes customers' faces and welcomes regulars. A camera at the shop entrance tells visitors apart by face and lets the owner know: "That's the person who had the tonteki last time, the one we haven't seen for three months." I meant to have a machine help with the job a small shop's owner does in their head: remembering faces, names, and preferences.

But soon after I started building, I realized this was a system entrusted with something very heavy. Faces. Attributes. Visit history. A customer's character. All of it is information that can never be taken back once it leaks.

What came to my mind then was Seicho Matsumoto's "Black Leather Notebook." A record shown to no one, yet certainly existing. A ledger that, once opened, sets people's lives and deaths in motion. Isn't that exactly what I am trying to build?

In Italian, "notebook" is Agenda, and "black" is Nera. Put together: AgendaNera. The black leather notebook. That is how the name was decided first.

AgendaNera is still being built. It is the one I am building most carefully in the series.

And this naming was the trigger. If there is a black notebook, there can be notebooks of other colors. I would rebuild the mechanisms I used every day in my own shop into forms any shop can use, and release them one notebook at a time. That is the [Agenda series](https://bontallc.com/agenda?via=b2-en-{{FMT}}).

### 3-3　Adding Notebooks, One at a Time

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
| AgendaTurno |  |  |  |

Which notebook suits which kind of shop? The Time Clock is for shops with two or more staff who manage attendance on paper or in LINE ⟦Japan's most widely used messaging app⟧. The Profit Planner is for people about to open a shop, and for those who want to review their numbers because rent or costs have changed. The Next Stop Guide is for shops centered on meals that want to send customers on to the next place early. The Light Notebook is for independent shops whose closing runs later or earlier than planned. Recipe Costing is for shops where the recipes are in your head but you have never worked out a cost ratio.

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

【Figure 3-2】The Agenda series introduction page ⟦The screen is in Japanese.⟧

【Figure 3-3a】Introduction to the Time Clock ⟦The screen is in Japanese.⟧

【Figure 3-3b】Introduction to the Profit Planner ⟦The screen is in Japanese.⟧

【Figure 3-3c】Introduction to the Next Stop Guide ⟦The screen is in Japanese.⟧

【Figure 3-4】The Time Clock's clock-in screen. Just tap your name (synthetic data) ⟦The screen is in Japanese.⟧