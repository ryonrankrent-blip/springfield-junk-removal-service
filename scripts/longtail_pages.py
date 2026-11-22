"""Long-tail cleanout pages added for the 2026-11-22 on-page brief.

Imported by build-site.py. Does not change phone, form, or tracking values.
"""


def longtail_pages(phone, cleanouts, commercial, cleanout_service):
    return [
        _storage(phone, cleanouts, cleanout_service),
        _basement(phone, cleanouts, cleanout_service),
        _attic(phone, cleanouts, cleanout_service),
        _office(phone, commercial),
    ]


def _storage(phone, cleanouts, cleanout_service):
    return {
        "file": "storage-unit-cleanout-springfield-mo.html",
        "href": "/storage-unit-cleanout-springfield-mo",
        "dedicated": True,
        "parents": cleanouts,
        "nav_href": "/cleanouts-springfield-mo",
        "crumb": "Storage unit cleanout",
        "title": "Storage Unit Cleanout in Springfield, MO",
        "description": "Storage unit cleanouts in Springfield, MO. We empty units, haul junk, and can meet a cutoff date. Call (417) 242-5370.",
        "h1": "Storage Unit Cleanout in Springfield, MO",
        "lede": (
            f"We empty storage units in Springfield, Missouri: furniture, boxes, mattresses, and leftover household junk. "
            f"Call {phone} with the facility, the unit size, and the date the unit has to be clear. "
            f"We do not pay the storage bill, and we do not negotiate with the facility."
        ),
        "service": cleanout_service,
        "quote_heading": "Quote a storage unit cleanout",
        "quote_copy": "<p>Name the facility area of town, the unit size, a drive-up or an indoor hallway, the gate process, and the date it has to be empty.</p>",
        "faqs": [
            (
                "Do you empty storage units in Springfield, MO?",
                "Yes. We haul the contents of a storage unit when you can let us in. Call (417) 242-5370 with the unit size and the date it has to be clear.",
            ),
            (
                "Can you meet a storage cutoff or auction date?",
                "Tell us the date. We will say the first time we can be there. We do not promise a same-day empty-out, and a call does not stop a facility's own deadline.",
            ),
            (
                "Do you need a gate code?",
                "Usually, yes. Say how the facility lets a truck in, whether the unit is drive-up, and how far the walk is from the nearest place a truck can stop.",
            ),
            (
                "Will you decide what to keep from the unit?",
                "No. You mark what stays with you and what goes on the truck. We do not buy the contents or run a storage auction.",
            ),
            (
                "What will you not take out of a storage unit?",
                "Hazardous waste, paint, fuel, ammunition, and medical waste stay out of the truck. Tell us if the unit smells of chemicals or if anything is leaking.",
            ),
        ],
        "body": f"""
<section>
<div class="wrap">
<h2>What a storage unit cleanout is</h2>
<p>A storage unit cleanout is a haul from a rented unit, not from a house. People book it when a unit has to be empty before a payment deadline, after a move that never got unpacked, or when a relative's unit is still full. The job is the contents. We do not rent units, and we are not the storage company. Call {phone} and describe what you can see when the door opens.</p>
<p>Springfield has indoor hallway buildings and rows of drive-up doors, including along the commercial strips and near the colleges. The building type changes the work more than the neighborhood name. A drive-up door lets us load closer to the truck. An indoor unit can mean a freight elevator, a long corridor, and a facility rule about how long a truck may sit at the curb. Tell us which one you have.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>Unit size</h3><p>A 5-by-5 locker, a 5-by-10 closet, a 10-by-10 room, and a 10-by-20 or 10-by-30 bay are different volumes. The size painted on the door is more useful than "pretty full." If the unit is packed to the ceiling, say that too. Height is part of the load.</p></article>
<article class="card"><h3>What is usually inside</h3><p>Couches, mattresses, dressers, boxes, lamps, and holiday bins. A single piece can be <a href="/furniture-removal-springfield-mo">furniture removal</a> or <a href="/mattress-removal-springfield-mo">mattress removal</a>. A unit of mixed leftovers is this page. Appliances belong on the list if a refrigerator or washer is in there.</p></article>
<article class="card"><h3>What you keep</h3><p>Papers, photos, and anything you still want come out with you before we load, or you point them out while we are there. We do not sort a unit for value, and we do not appraise furniture.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>Facility rules we need before we quote</h2>
<p>Storage companies set their own hours, truck rules, and insurance requirements for vendors. We follow the rules you pass on, and we will tell you if a rule changes whether we can do the job. Ask the office, then tell us:</p>
<ul>
<li>The gate code, lock code, or whether someone from the office has to walk us in.</li>
<li>The hours a truck is allowed, and whether weekends are different.</li>
<li>Drive-up door or indoor hallway, and which floor.</li>
<li>How far we carry items to a legal place to park.</li>
<li>Whether the facility requires the unit to be swept or the lock left a certain way. Sweeping the dust out is not part of a junk haul unless we include it in the quote.</li>
</ul>
<p>We do not cut locks. If the facility has already cut the lock for an auction or a lien process, the person who books the haul needs the right to empty the unit. We do not decide who owns the contents.</p>
</div>
</section>
<section>
<div class="wrap split">
<div>
<h2>Cutoff dates</h2>
<p>If the office gave you a date, put that date in the message. We will tell you the first opening we have. Same-day is sometimes possible and is not a promise. A form does not hold the unit, and it does not pause the facility's clock. If you are buying a unit at auction, say so. The person who meets us still needs the right to empty it.</p>
<p>Pricing follows the volume, the weight, and the carry, the same way a <a href="/junk-removal-cost-springfield-mo">house or garage quote</a> does. A mattress or an appliance on top of boxes is an add-on you should name. We do not publish a price per unit size.</p>
</div>
<div class="panel">
<h2>Related cleanouts</h2>
<p>A garage at the house is a <a href="/garage-cleanout-springfield-mo">garage cleanout</a>. Stored junk under the house is a <a href="/basement-cleanout-springfield-mo">basement cleanout</a>. A pull-down stair full of boxes is an <a href="/attic-cleanout-springfield-mo">attic cleanout</a>. The hub for all of those is <a href="/cleanouts-springfield-mo">property cleanouts</a>.</p>
</div>
</div>
</section>
<section>
<div class="wrap">
<h2>Items that stay out of a storage haul</h2>
<p>Paint, fuel, solvents, ammunition, and anything leaking stay in the unit or go to a drop-off that accepts them. Springfield's household chemical options are on the <a href="/springfield-junk-disposal-guide">pickup or drop-off page</a>. We will not haul a unit we cannot see. If you are out of town, someone with the code needs to be there, or you need to tell us how the facility will let us in and what is marked to go. Photos of the open door help the quote match the pile.</p>
<p>Usable furniture is not automatically a donation. If you want a charity to take something, call that organization and confirm before pickup day. We haul what is left. We are not a donation center, and we do not promise a recycling outcome for mattresses left in a unit.</p>
</div>
</section>
""",
    }


def _basement(phone, cleanouts, cleanout_service):
    return {
        "file": "basement-cleanout-springfield-mo.html",
        "href": "/basement-cleanout-springfield-mo",
        "dedicated": True,
        "parents": cleanouts,
        "nav_href": "/cleanouts-springfield-mo",
        "crumb": "Basement cleanout",
        "title": "Basement Cleanout in Springfield, MO",
        "description": "Basement cleanouts in Springfield, MO for stored junk, old furniture, and wet-damaged items. Call (417) 242-5370 for a quote.",
        "h1": "Basement Cleanout in Springfield, MO",
        "lede": (
            f"We haul stored junk, old furniture, and wet-damaged household items from basements in Springfield, Missouri. "
            f"Call {phone} and say whether the stairs are inside the house or through an outside door. "
            f"This is not mold remediation, and it is not a plumbing repair."
        ),
        "service": cleanout_service,
        "quote_heading": "Quote a basement cleanout",
        "quote_copy": "<p>Say how full the basement is, whether items are wet, and whether the stairs are inside or through a bulkhead. Name anything that must stay, such as a water heater.</p>",
        "faqs": [
            (
                "Do you clean out basements in Springfield, MO?",
                "Yes. We carry stored junk, furniture, and bagged household items up from Springfield basements. Call (417) 242-5370 and describe the stairs and how full the space is.",
            ),
            (
                "Do you take water-damaged furniture and cardboard?",
                "We can haul wet furniture, soggy boxes, and household goods that are not hazardous. Bag loose debris if you can. We do not dry the basement, treat mold, or fix the leak.",
            ),
            (
                "Will you remove the water heater or furnace?",
                "Only if you list it and we include it in the quote. A water heater, furnace, or sump pump is not assumed to be junk. Say if it is disconnected.",
            ),
            (
                "Is a basement cleanout the same as a house cleanout?",
                "No. This page is the basement when the rest of the house is staying. If every floor goes, use the house cleanout page and include the basement in that description.",
            ),
            (
                "What should I do with paint in the basement?",
                "Leave it out of the haul. Paint, solvents, and fuel are not basement junk we take. Springfield's household chemical drop-off is listed on the pickup or drop-off page.",
            ),
        ],
        "body": f"""
<section>
<div class="wrap">
<h2>A basement pile is its own job</h2>
<p>People call when the basement became the place everything went: holiday bins, a broken couch, a spare mattress, boxes from a move ten years ago, and shelves that sag. The rest of the house can stay as it is. That is a basement cleanout. If you are emptying every floor, book a <a href="/house-cleanout-springfield-mo">house cleanout</a> and include the basement in the same description so we do not quote the lower level alone. Call {phone} with a plain account of the space.</p>
<p>Springfield houses vary. Some have a full basement under the main floor. Some have a partial basement, a low cellar, or only a crawl space. A crawl space is not a cleanout we can quote from the word "basement." Tell us the ceiling height and whether an adult can stand. If you have to crawl, say that before we schedule.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>Stairs and the path up</h3><p>Interior stairs from a kitchen or hall are the usual path. An outside bulkhead or walk-out door can be easier if it opens and a truck can get near it. Count the turns. A couch that came down in pieces may have to leave in pieces. Tell us if the handrail is loose or the stairs are open on one side.</p></article>
<article class="card"><h3>What we carry up</h3><p>Boxes, shelving, furniture, mattresses, bagged trash, and old exercise equipment you want gone. One mattress is also described on the <a href="/mattress-removal-springfield-mo">mattress removal</a> page. A washer and dryer pair is <a href="/appliance-removal-springfield-mo">appliance removal</a> if that is the whole job, or an add-on if the basement is otherwise full.</p></article>
<article class="card"><h3>What usually stays</h3><p>The water heater, furnace, electrical panel, sump pump, and any plumbing that is still in use stay put unless you name them and we agree they are part of the haul. We do not disconnect gas or water as a default.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>Wet basements and damaged belongings</h2>
<p>A Springfield basement can take on water in a heavy rain. Wet cardboard, stained furniture, and carpet pads can still be hauled if they are household junk and not a hazardous material. Tell us they are wet. Weight goes up when boxes have soaked up water, and that changes the quote. We load what you show us. We do not run fans, cut out drywall, or claim to remove mold. If the leak is still active, say so. We may need the water stopped before a haul makes sense, and we do not do that repair.</p>
<p>Musty is not the same as a chemical spill. Paint cans, old pesticides, and fuel cans are common on basement shelves and stay off the truck. Those belong at a household chemical drop-off. Links are on the <a href="/springfield-junk-disposal-guide">pickup or drop-off page</a>. If you are not sure what a container is, leave it out of the pile and tell us it is there so we do not pack it by mistake.</p>
</div>
</section>
<section>
<div class="wrap">
<h2>How the basement quote is built</h2>
<p>We price the volume, the weight, and the carry up the stairs. A few boxes by the stairs and a basement packed wall to wall are different jobs. A long walk from the stair door to the street, a narrow side yard, or parking only in an alley belongs in the description. There is no basement rate card. The factors are the same ones on the <a href="/junk-removal-cost-springfield-mo">junk removal cost</a> page, applied to a below-grade room.</p>
<p>Same-day is sometimes open. Call with the day you need and we will tell you the first time we can be there. We do not promise same-day service. Someone needs to let us in and point out what stays, especially utilities.</p>
</div>
</section>
<section>
<div class="wrap">
<h2>Basement, garage, or attic</h2>
<p>If the overflow is in the garage instead of under the house, use the <a href="/garage-cleanout-springfield-mo">garage cleanout</a> page. Boxes above the ceiling, reached by a pull-down ladder, are an <a href="/attic-cleanout-springfield-mo">attic cleanout</a>. A rented unit off the property is a <a href="/storage-unit-cleanout-springfield-mo">storage unit cleanout</a>. You can book more than one space on the same visit if you describe each space. The <a href="/cleanouts-springfield-mo">cleanouts</a> page lists the other property types, including estates and apartments.</p>
</div>
</section>
""",
    }


def _attic(phone, cleanouts, cleanout_service):
    return {
        "file": "attic-cleanout-springfield-mo.html",
        "href": "/attic-cleanout-springfield-mo",
        "dedicated": True,
        "parents": cleanouts,
        "nav_href": "/cleanouts-springfield-mo",
        "crumb": "Attic cleanout",
        "title": "Attic Cleanout in Springfield, MO",
        "description": "Attic cleanouts in Springfield, MO. We carry items down and haul them away. Call (417) 242-5370.",
        "h1": "Attic Cleanout in Springfield, MO",
        "lede": (
            f"We carry boxes, old furniture, and stored household junk down from attics in Springfield, Missouri, and haul them away. "
            f"Call {phone} and say whether the opening is a pull-down stair, a fixed stair, or a hatch. "
            f"We do not remove insulation, and we do not take asbestos."
        ),
        "service": cleanout_service,
        "quote_heading": "Quote an attic cleanout",
        "quote_copy": "<p>Describe the stair or hatch, about how full the attic is, and whether any piece has to come apart to fit through the opening.</p>",
        "faqs": [
            (
                "Do you clean out attics in Springfield, MO?",
                "Yes. We carry stored items down and haul them. Call (417) 242-5370 and describe the stair or hatch and how much is up there.",
            ),
            (
                "What if the only access is a pull-down ladder?",
                "Tell us. A pull-down ladder limits the size of what can come down and how we carry it. A broken or missing ladder needs to be described before we quote.",
            ),
            (
                "Do you take insulation out of the attic?",
                "No. We haul belongings you stored, not the insulation. If you think insulation might contain asbestos, leave it in place and do not ask us to bag it.",
            ),
            (
                "Can one piece of furniture come down from the attic?",
                "Yes, if it fits through the opening or can come apart. A single dresser with the rest of the attic staying is still an attic job because of the carry. Name the piece.",
            ),
            (
                "Is an attic cleanout part of a garage cleanout?",
                "Only if you are booking both spaces. A garage and an attic are different carries. Describe each one so the quote matches both piles.",
            ),
        ],
        "body": f"""
<section>
<div class="wrap">
<h2>Attic cleanouts start with the opening</h2>
<p>An attic cleanout is the carry down, then the haul. The opening decides what is possible. A fixed stair, like a real staircase to a finished or semi-finished attic, is closer to moving items between floors. A pull-down ladder in a hallway is narrower, steeper, and often the only way in. A scuttle hatch with no stair is harder still. Call {phone} and name which one the house has. If the ladder is broken, stuck, or missing, say that. We do not install a new stair.</p>
<p>Older Springfield houses often store luggage, holiday decorations, and a spare bed above the ceiling. Newer houses may have a truss attic with no floor, only joists and insulation. We need a surface that can be walked. If the "floor" is joists with insulation between them, tell us. We will not step through a ceiling to reach a box.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>What we carry down</h3><p>Boxes, bins, luggage, small furniture, bagged clothing you are discarding, and holiday items you do not want. Tell us if a dresser, a table, or a headboard has to be taken apart to fit the opening. We quote the pieces you name.</p></article>
<article class="card"><h3>Heat, dust, and low clearance</h3><p>A Springfield attic in summer is hot, and the work is slower. Low headroom and knee walls mean we cannot stand everywhere. A description of how far you can walk from the opening helps more than a guess at the square footage.</p></article>
<article class="card"><h3>What we leave</h3><p>Insulation, roof decking, wiring, and bathroom fans stay. We are not an insulation crew or a roofer. Belongings you still want can be moved to the side if you mark them before we arrive.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>Furniture that will not fit the hatch</h2>
<p>A bookcase or a tabletop that went up in pieces can come down in pieces if the fasteners still work. A solid piece wider than the opening cannot. Measure the opening if you can, or send a photo of the stair and of the largest item. We would rather quote a disassembly than discover it on site and stop. One couch or dresser that is already on a living-room floor is <a href="/furniture-removal-springfield-mo">furniture removal</a>, not an attic job. The attic page is for items that are still up there.</p>
<p>Mattresses stored in an attic can go on the same haul. Name the size. If the mattress is the only item and it is already downstairs, use <a href="/mattress-removal-springfield-mo">mattress removal</a>. City mattress recycling, if you haul it yourself, is a separate fee on the city's page, linked from the <a href="/springfield-junk-disposal-guide">pickup or drop-off page</a>.</p>
</div>
</section>
<section>
<div class="wrap">
<h2>Insulation and materials we will not bag</h2>
<p>We do not vacuum, remove, or bag attic insulation. Some older insulation materials are not ordinary trash. If you suspect asbestos, leave it alone and do not have us carry it out with the boxes. We do not take asbestos. The same rule covers vermiculite or any loose fill you cannot identify. Point it out so we stay out of that area. Paint, pesticides, and fuel do not belong in an attic haul either.</p>
<p>The quote is the volume of belongings, the weight, and the difficulty of the ladder or stair. There is no attic flat rate. See <a href="/junk-removal-cost-springfield-mo">what changes a junk removal quote</a>. We do not promise same-day service. Call with the day you hope for and we will tell you the first opening.</p>
</div>
</section>
<section>
<div class="wrap">
<h2>How an attic fits the other cleanouts</h2>
<p>Garages, basements, and attics are the three places Springfield houses hide storage. The <a href="/garage-cleanout-springfield-mo">garage cleanout</a> page is the bay at ground level. The <a href="/basement-cleanout-springfield-mo">basement cleanout</a> page is below grade. A unit you rent off site is a <a href="/storage-unit-cleanout-springfield-mo">storage unit cleanout</a>. If the whole house is being emptied, including the attic, start with <a href="/house-cleanout-springfield-mo">house cleanout</a> or <a href="/estate-cleanout-springfield-mo">estate cleanout</a> and mention the attic so it is not left out of the volume. All of those links sit on the <a href="/cleanouts-springfield-mo">cleanouts</a> hub.</p>
</div>
</section>
""",
    }


def _office(phone, commercial):
    return {
        "file": "office-cleanout-springfield-mo.html",
        "href": "/office-cleanout-springfield-mo",
        "dedicated": True,
        "parents": commercial,
        "nav_href": "/commercial-junk-removal-springfield-mo",
        "crumb": "Office cleanout",
        "title": "Office Cleanout in Springfield, MO",
        "description": "Office cleanouts in Springfield, MO for desks, chairs, and cubicle tear-outs. Call (417) 242-5370 for a quote.",
        "h1": "Office Cleanout in Springfield, MO",
        "lede": (
            f"We haul office furniture and cubicle tear-outs from Springfield, Missouri workplaces. "
            f"Desks, task chairs, filing cabinets, and panel systems. Call {phone} with the floor, the elevator rules, and whether the suite is still occupied. "
            f"Broader store and job-site junk stays on the commercial page."
        ),
        "service": "Commercial junk or construction debris",
        "quote_heading": "Quote an office cleanout",
        "quote_copy": "<p>Include the floor, elevator or stair, after-hours limits, and a count of desks, cabinets, and cubicle panels. Say if computers stay.</p>",
        "faqs": [
            (
                "Do you clean out offices in Springfield, MO?",
                "Yes. We haul desks, chairs, filing cabinets, and cubicle panels from Springfield offices. Call (417) 242-5370 with the floor and the hours we can get in.",
            ),
            (
                "Do you tear out cubicles?",
                "We can take cubicle panels, work surfaces, and pedestals apart when that is part of the quote. Tell us the panel height and about how many stations. We do not patch walls or recarpet the suite.",
            ),
            (
                "Are full filing cabinets harder to move?",
                "Yes. A cabinet full of paper is a heavy item. Empty it if you can, or tell us it is full so the quote includes that weight. We do not shred documents.",
            ),
            (
                "Do you wipe computers or certify recycling?",
                "No. We do not wipe drives, and we do not issue a recycling or destruction certificate. Remove data before pickup, or pull the equipment from the haul.",
            ),
            (
                "Is an office cleanout the same as construction debris?",
                "No. Drywall, lumber, and flooring from a remodel are construction debris. This page is furniture and cubicles. A mixed suite can include both if you describe both.",
            ),
        ],
        "body": f"""
<section>
<div class="wrap">
<h2>Office furniture and cubicles, not every commercial load</h2>
<p>This page is for an office: a suite, a floor, or a few rooms of desks and panels. A store closeout, a warehouse of mixed junk, or a remodel pile belongs on <a href="/commercial-junk-removal-springfield-mo">commercial junk removal</a>. Drywall, lumber, and flooring are <a href="/construction-debris-removal-springfield-mo">construction debris</a>. Call {phone} if the load is mostly furniture and workstations and you need them gone so the space can be re-leased or reused.</p>
<p>Springfield offices sit downtown, along Glenstone, Sunshine, Kearney, and in smaller buildings scattered through the city. The address matters less than the path from the suite to the truck. A ground-floor office with a door to the parking lot is a different carry from a downtown suite that requires a freight elevator and a loading dock reservation.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>Desks and chairs</h3><p>Workstations, reception desks, conference tables, task chairs, and side chairs. Particle-board desks that wobble still count. Tell us if a desk is built in or bolted to a wall. Built-ins may be debris rather than furniture. Say which.</p></article>
<article class="card"><h3>Cubicle tear-outs</h3><p>Panels, tiles, work surfaces, overhead bins, and pedestals. A tear-out means we take the station apart enough to carry it. It does not mean we repair the floor, paint, or remove cable from the ceiling. Name the approximate station count. "The whole floor" is not a count.</p></article>
<article class="card"><h3>Cabinets and paper</h3><p>Lateral and vertical files are heavy when they are full. We can haul them full if you say so. We do not sort records, and we do not shred. If files must stay for legal reasons, mark the cabinets that stay before we arrive.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>Building access in Springfield</h2>
<p>Tell us who will let us in. That is usually an office manager, a property manager, or the tenant on the way out. We do not have master keys, and we do not sign a building's vendor packet unless that step is agreed before the day of the haul. Useful details:</p>
<ul>
<li>Floor number, and whether the passenger elevator can be used or only a freight car.</li>
<li>Dock hours, a certificate the building asked for, and any after-hours window.</li>
<li>Where a truck may park, and for how long.</li>
<li>Protection the building wants on floors or elevator walls. We will say if that changes the quote.</li>
<li>Whether the suite is still staffed. Working around people is slower than an empty office.</li>
</ul>
<p>A property-manager turnover of an apartment is not this page. That job is an <a href="/apartment-cleanout-springfield-mo">apartment cleanout</a> or an <a href="/eviction-cleanout-springfield-mo">eviction cleanout</a>.</p>
</div>
</section>
<section>
<div class="wrap">
<h2>Electronics and what we will not certify</h2>
<p>Monitors, docks, printers, and small computers can go on the list. We haul the hardware. We do not wipe data, destroy drives, or give you a certificate that anything was recycled. Pull drives or clear accounts before pickup if the data matters. Copiers and large printers need their own line in the quote because of weight. We do not take toner spills, batteries loose in a box, or chemicals from a janitor's closet as if they were office junk.</p>
<p>There is no office price list. Volume, weight, stairs or elevator time, and the hours we are allowed in the building set the quote. A mattress left in a break room or a refrigerator in a kitchenette should be named; those add-ons are explained on the <a href="/junk-removal-cost-springfield-mo">cost page</a>. We do not promise same-day service. If a lease ends on a date, tell us that date and we will tell you the first time we can be there.</p>
</div>
</section>
<section>
<div class="wrap">
<h2>Where this page stops</h2>
<p>Kitchenettes with household appliances can be included if you list them. A full restaurant or a retail fixture pull is commercial junk, not an office cleanout. Construction that has already opened walls is construction debris. If you are clearing a house that happened to contain a desk, use <a href="/residential-junk-removal-springfield-mo">residential junk removal</a> or a <a href="/house-cleanout-springfield-mo">house cleanout</a>. The commercial hub remains the right start when the load is mixed and you are not sure which page fits. Call {phone} and describe the suite in a few sentences.</p>
</div>
</section>
""",
    }
