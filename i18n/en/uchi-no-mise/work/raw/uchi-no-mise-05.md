### 4-4　Common Navigation, and the Failure of the Word "Front Door"

So that users can get from any product to the others, I gave every product a shared navigation menu. It is the path that lets a bar owner using Time Clock ask a question in Support Guide, or go and look at the other notebooks.

There is a small failure story behind this shared navigation.

In the first version, I had placed a link that said "Back to the front door." That was because, internally, I called AgendaHub the "front door." But when I checked on a real device, something was off. Two links, "Back to the front door" and "See the Agenda series," jumped to the same place. On top of that, the support link sat above the everyday work menu, so the order of importance was backwards. And above all, the words "front door" mean nothing to an owner using the product for the first time. It was the maker's own internal language.

So I reset the principles. Order the items by how close they are to the user's purpose: everyday work at the very top, links leading outside at the very bottom. Even a link meant to win new users never goes above the work. The boundary must be explainable with a single line. Write the wording in the user's language, not internal language. Never put more than one link that jumps to the same place. I scrapped "Back to the front door" and merged everything into a single link, "See the other Agenda notebooks."

In Chapter 2, I wrote about learning the language of the UI. That was language for the owner to use when talking to the AI. This is the opposite: language the maker uses to talk to the user. In both cases, it was about fitting your words to the person you are speaking to.

【Figure 4-4】The shared navigation after the fix. Work is at the top, and the links leading outside are at the very bottom ⟦The screen is in Japanese.⟧

### 4-5　The Foundation Costs $35 a Month

The database cost of the whole foundation described in this chapter is about $35 a month. The paid plan that includes the production project is $25, and the project for the test environment is $10.

This, too, was not the amount from the start. At one point I was paying $45 a month. The development database for a face recognition product was still being billed even though I wasn't using it. I moved it to the free tier and stopped it, deleted another project I wasn't using, and that is how it got to the current amount.

I also keep an eye on the cost of AI. The work of the AI that writes programs is billed by the amount of tokens (the unit of text the AI reads and writes). I avoid concentrating costs by having the work window stick to the role of coordinator and leaving the implementation itself to a different AI with a separate cost allowance. For the generative model in the chat window as well, I look at the price and choose what is necessary and sufficient. Even if a higher-tier model costs only $1 more per month, I choose by asking "is it enough?"

If you build small, even small sales can sustain you. The monetization story in Chapter 3 is supported by how small the cost of this foundation is.

### 4-6　The Coordinating AI, and the Person Who Makes the Call

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

The continuation of this chapter (the next notebooks I build, and the lessons I added to the manual) is on note and X. note https://note.com/bontallc／X https://x.com/tamuro\_hnakano

## Chapter 5: A Small Bar's Future

### 5-1　From Zatta Gohan to Tamuro

I entered the food and drink business when I was 39.

The trigger was a neighborhood bar called Zatta. Once a month, sometimes every other week, they let me serve meals there. I had taught myself to cook for a long time, but now I had a place where people ate my food and were happy. That was my original experience.

In 2014, I opened a restaurant called Zatta Gohan in Arai-Yakushi. It was a small place that served set meals. I ran it for seven years.

In Arai-Yakushi, though, I felt a limit on the number of customers. Then I found a property in Higashi-Nakano ⟦a residential neighborhood in western Tokyo, just west of Shinjuku⟧. It takes less than a minute to walk from the east exit of the station. Even on a rainy day, you can get there without getting very wet.

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

### 5-2　Quatre Épices' Hamburger Curry

Tamuro is a night-time bar. During the day, the space is empty.

Using that time, I started Quatre Épices in January 2024. It is a hamburger curry shop that operates only at lunchtime in the same place, and the staff run it.

Quatre Épices means "four spices" in French. True to the name, rather than layering on lots of spices, we choose and narrow them down to make the outline of the flavor clear. The curry uses no flour; it is finished with the natural thickness of the vegetables and meat themselves. Satisfaction when you finish eating, and no heaviness in the stomach. And harmony with the hamburger. I designed it on those three premises.

We are particular about how the hamburger is cooked. We set the blend so that it comes out crisp outside and fluffy inside, and we cook to suit that blend. The way of cooking with heat that I learned at night at Tamuro serves the daytime plate too.

Prices, business days and hours can change, so please check Tamuro's Instagram (https://www.instagram.com/tamuro.higashinakano/) for the latest information.

Quatre Épices also runs a children's cafeteria in the same place. It is an activity that uses the existing bar's facilities and purchasing to serve meals to children in the neighborhood. Through that connection, we also built a relationship with the local community center. We sometimes serve curry and sandwiches at local sports events, community center events and Bon dance festivals.

To be honest, using the daytime hours has not all gone well. I created days for daytime drinking and rented the space to other people, but customers did not come as I hoped. The bar's appeal comes across differently when the owner is there at night and when only the daytime staff are there. Growing the daytime shop with an appeal different from the night shop's is still an unfinished task.

### 5-3　Bonta LLC: Two Pillars

The small company that runs Tamuro and Quatre Épices is Bonta LLC. I am its managing member.

The company has two pillars. One is food and drink: Tamuro and Quatre Épices. The other is IT: development of the Agenda series, and consulting.

Food and drink and tools differ in how they earn money. Supporting the company with two pillars of different natures is the form I have in mind.

And the two pillars supply each other with materials. Trouble at the bar becomes the seed of a tool. What I learn from building tools comes back into running the bar. The Light Notebook was born from closing times running late, and the extended-hours records from the Light Notebook become the basis for profit estimates and shifts. The "questions we could not answer" that pile up in the chat window improve the bar's guidance. This cycle is the reason I can manage both the bar and development on my own.

I am not thinking of making the company bigger. Small, many, and cheap. That is the shape of this company.

### 5-4　Writing as Raku Bonta

When I write and publish, I use the pen name "Raku Bonta." I wrote this book under that name too.

My previous book, *Running a Bar Alone, and AI Arrived Beside Me*, was a book about generative AI. It ranked number one in Amazon's time management category and was read by many people. This book is its sequel.

Besides books, I also write on note. I write about the bar's efforts with AI, what I found on a training trip, the progress of publishing my books, and the Agenda series. You can follow the continuation I couldn't fit in this book on note (https://note.com/bontallc).

For me, writing is also a way to put both the bar and development into words and check them. As I wrote in Chapter 1, the first knowledge of the chat window "T-AI-MURO" was built from words I had been leaving on X. What I had written down became material for the AI. From now on, too, what I write will return to both the bar and the AI.

There is one more thing I have decided about writing. I don't announce unfinished things with "coming soon." I finish it, make an introduction page, and only then put it out. I believe keeping to that order is what earns a small company trust.

### 5-5　The Future of the Independent Shop

Finally, I'll gather what I've written in this book into a single picture.

【Figure 5-1】The big picture of what this book has described. A small bar opens its own window (the first story), and turns its troubles into tools to hand to other bars (the second story) ⟦The screen is in Japanese.⟧

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

The Agenda series: https://bontallc.com/agenda?via=b2-en-{{FMT}}

Follow my activities: note https://note.com/bontallc／X https://x.com/tamuro\_hnakano

If you are ever in Higashi-Nakano, drop by Tamuro. You can reserve through the reservation site, through the chat window "T-AI-MURO" on the site, and of course through your own AI.

Tamuro's reservation site: https://tamuroreservation.vercel.app/?src=b2-en-{{FMT}}

Tamuro's Instagram: https://www.instagram.com/tamuro.higashinakano/

For those who want to try booking from AI. The connection address for Tamuro's MCP server is the following URL.

https://tamuroreservation.vercel.app/api/mcp

In the settings of your AI (such as Claude or ChatGPT), open the screen for adding external tools (connectors, MCP servers) and register this URL. How to register varies by AI and over time, so the safest approach is to look up "MCP" or "connector" in each AI's help. Depending on the plan you have, you may not be able to connect an MCP server of your own choosing. Once registered, ask your AI, "Is Tamuro open tonight?" It will check the open slots and prices and guide you to the reservation page. The confirm button is pressed by you.

For those who came after reading the book. When you reserve, please enter the coupon code "BOOK." We will serve you one drink on the house for your first round. If you came without a reservation, just say "I saw the book" when you place your first order. We will serve you the same drink. It is a small device that lets me count how many people came from the book.

You can come in without a reservation. Even alone, you won't stand out. You may even end up chatting happily with the person next to you.

I'm waiting for you at a place where people gather.

Raku Bonta

### References

- OpenAI Help Center, "ChatGPT — Release Notes," August 10, 2026, "Restaurant reservations in ChatGPT" https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- Alpaca, "Alpaca MCP Server" (an example of an MCP server in the US that lets AI place orders for stocks and other securities) https://docs.alpaca.markets/docs/alpaca-mcp-server
- The "death of SaaS" debate: Satya Nadella's remarks on the BG2 podcast (December 2024), the sharp drop in software stocks in February 2026 and what it was called, and Jensen Huang's rebuttal were drawn from the following reports and commentaries. https://www.longangle.com/alts-education/software-ai ／ https://www.fastcompany.com/91504460/everything-youve-heard-about-the-saaspocalypse-is-wrong ／ https://en.thairath.co.th/money/tech\_innovation/tech\_companies/2916811