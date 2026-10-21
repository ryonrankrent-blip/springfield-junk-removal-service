/*
 * Springfield Junk Removal Service — lead event tracking
 *
 * Events:
 *   click_call          tel: click on (417) 242-5370
 *   click_quote_button  quote CTA (#quote)
 *   submit_lead_form    Formspree form submit
 *
 * Delivery:
 *   - dataLayer push for the existing GTM container GTM-GDJF54DV
 *   - gtag, only after GA4_MEASUREMENT_ID_PROPERTY_541475893 is a real G- ID
 *
 * GA4 PLACEHOLDER
 *   Property 541475893 measurement ID was not found in this repo or git history.
 *   Leave the string empty. Do not guess.
 *   Docs mention GTM destination G-GWT8GR7QJC. That ID is not recorded as
 *   property 541475893, so it is not installed here as a direct GA4 tag.
 */
(function () {
  "use strict";

  var MARKET = "Springfield, MO";
  var NICHE = "Junk Removal";
  var PHONE = "4172425370";

  // PLACEHOLDER: GA4 measurement ID for property 541475893. Not found. Do not guess.
  var GA4_MEASUREMENT_ID_PROPERTY_541475893 = "";

  var directGa4 = false;

  function installGa4(measurementId) {
    if (!/^G-[A-Z0-9]+$/.test(measurementId)) return;
    var script = document.createElement("script");
    script.async = true;
    script.src = "https://www.googletagmanager.com/gtag/js?id=" + measurementId;
    document.head.appendChild(script);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () {
      window.dataLayer.push(arguments);
    };
    window.gtag("js", new Date());
    window.gtag("config", measurementId);
    directGa4 = true;
  }

  installGa4(GA4_MEASUREMENT_ID_PROPERTY_541475893);

  function sendEvent(name, params) {
    params = params || {};
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(merge({ event: name }, params));
    if (directGa4 && typeof window.gtag === "function") {
      window.gtag("event", name, params);
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

    var quoteLink = closestEl(e.target, 'a[href*="#quote"]');
    if (quoteLink) {
      sendEvent("click_quote_button", {
        page_path: location.pathname,
        link_text: (quoteLink.textContent || "").trim(),
        destination: quoteLink.getAttribute("href") || ""
      });
    }
  });

  document.addEventListener(
    "submit",
    function (e) {
      var form = e.target;
      if (!form || form.tagName !== "FORM") return;
      var action = form.getAttribute("action") || "";
      if (action.indexOf("formspree.io/f/mojzdkvg") === -1) return;

      var params = {
        page_path: location.pathname,
        market: MARKET,
        niche: NICHE
      };
      var serviceField = form.querySelector('[name="service"]');
      if (serviceField && serviceField.value) params.service = serviceField.value;
      sendEvent("submit_lead_form", params);
    },
    true
  );
})();
