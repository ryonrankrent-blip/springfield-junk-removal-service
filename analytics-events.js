/*
 * Springfield Junk Removal Service - lead event tracking
 *
 * Tracks: click_call, click_quote_button, submit_lead_form
 *
 * Analytics-agnostic by design:
 *   - If GTM is detected, events are sent via dataLayer.push (preferred).
 *   - Else if gtag (GA4) is detected, events are sent via gtag('event', ...).
 *   - If neither is installed yet, events are queued on window.dataLayer so they
 *     flush automatically once a GTM container is added later.
 *
 * NOTE: This file does NOT install GA4 or GTM and does NOT contain a Measurement
 * ID or container ID. Add your GA4 (gtag.js) or GTM snippet in each page <head>
 * for these events to be delivered to your analytics property.
 */
(function () {
  "use strict";

  var MARKET = "Springfield, MO";
  var NICHE = "Junk Removal";
  var PHONE = "4172425370";

  function sendEvent(name, params) {
    params = params || {};
    var hasGtm = typeof window.google_tag_manager !== "undefined";
    var hasGtag = typeof window.gtag === "function";

    if (hasGtm) {
      // Preferred path for GTM compatibility.
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push(merge({ event: name }, params));
    } else if (hasGtag) {
      window.gtag("event", name, params);
    } else {
      // Neither installed yet: queue on dataLayer so GTM can pick it up later.
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push(merge({ event: name }, params));
    }
  }

  function merge(target, source) {
    for (var key in source) {
      if (Object.prototype.hasOwnProperty.call(source, key)) {
        target[key] = source[key];
      }
    }
    return target;
  }

  function closestEl(node, selector) {
    var el = node && node.nodeType === 1 ? node : node && node.parentElement;
    return el && el.closest ? el.closest(selector) : null;
  }

  function digitsOnly(value) {
    return (value || "").replace(/[^0-9]/g, "");
  }

  document.addEventListener("click", function (e) {
    // 1) Phone clicks (any tel: link to the business number)
    var telLink = closestEl(e.target, 'a[href^="tel:"]');
    if (telLink) {
      var href = telLink.getAttribute("href") || "";
      if (digitsOnly(href) === PHONE) {
        sendEvent("click_call", {
          page_path: location.pathname,
          link_text: (telLink.textContent || "").trim(),
          destination: href,
          phone_number: PHONE
        });
      }
      return;
    }

    // 2) Quote / contact buttons or links pointing at the form/contact section
    var quoteLink = closestEl(e.target, 'a[href*="#quote"], a[href*="#contact"]');
    if (quoteLink) {
      var dest = quoteLink.getAttribute("href") || "";
      sendEvent("click_quote_button", {
        page_path: location.pathname,
        link_text: (quoteLink.textContent || "").trim(),
        destination: dest
      });
    }
  });

  // 3) Formspree lead form submissions
  document.addEventListener(
    "submit",
    function (e) {
      var form = e.target;
      if (!form || form.tagName !== "FORM") return;
      var action = form.getAttribute("action") || "";
      if (action.indexOf("formspree.io") === -1) return;

      var params = {
        page_path: location.pathname,
        market: MARKET,
        niche: NICHE
      };

      var serviceField = form.querySelector('[name="service"]');
      if (serviceField && serviceField.value) {
        params.service = serviceField.value;
      }

      sendEvent("submit_lead_form", params);
    },
    true // capture so it runs before the form navigates away
  );
})();
