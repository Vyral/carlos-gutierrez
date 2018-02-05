---
layout: recruiting
title: Join Our Team
permalink: /join-our-team/
---
<div class="recruiting-photo">
   <span class="client-image-container">
    <img src="/img/headshot.jpg" alt="{{site.data.settings.client.name}}" class="client-image"/>
  </span>
<figcaption class="caption">{{site.data.settings.client.name}}</figcaption>
</div>
<h1>Join One of the Fastest Growing Real Estate Teams in {{site.data.settings.client.market}}</h1>
<h5>How would your life change if you consistently earned $60,000, $75,000, $100,000 or more as a full-time real estate agent?</h5>
<div class="recruiting-page">
<p>Dear real estate agent or frustrated employee:</p>
</div>
<h2 class="recruiting">Let's Make You More Money</h2>
<h4 class="recruiting">Request a phone call - it does not cost a dime to talk.</h4>
<form method="post" class="home-value cta-forms" action="http://formspree.io/{{site.data.settings.client.email}}" onsubmit="return setReturn()">
    <fieldset>
        <p id="thanks"></p>
<label for="firstname">First Name*</label>
<input type="text" name="firstname" required>
<label for="lastname">Last Name*</label>
<input type="text" name="lastname" required>
<label for="email">Email*</label>
<input type="text" name="name">
<label for="phone">Phone Number
</label>
<input type="tel" name="phone">
<!--11-->
<label for="city">City
</label>
<input type="text" name="city">
<label for="state">State
</label>
<input type="text" name="state">
<label for="employer">Current Employer
</label>
<input type="text" name="employer">
<label for="message">Why are you interested in this?
</label>
<textarea name="employer"></textarea>
<!-- submit! -->
<input class="submit light-light" type="submit" value="Apply Now" name="submitrecruitingForm">
<span class="asterisk">*</span>required
</fieldset>
<!-- Cloud cannon settings field -->
<div class="hidden">
<input type="hidden" name="_to" value="{{site.data.settings.client.email}}">
<input type="hidden" name="_subject" value="Recruiting Contact Request Message From Your Vyral Careers and Training Video Blog">
<input type="text" name="_gotcha">
</div>
</form>
