#!/usr/bin/env node
const puppeteer = require('puppeteer')
async function run() {
  const browser = await puppeteer.launch()
  const page = await browser.newPage()
  await page.goto('https://mikeallred.com')
  await page.screenshot({ path: 'screenshots/mikeallred.png' })
  browser.close()
}
run()
