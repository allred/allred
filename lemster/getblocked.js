#!/usr/bin/env node
import pkg from 'lemmy-js-client';
const { LemmyHttp, Login } = pkg;
import * as https from "http"
//const https = require('https')
//import https
/*
let https
try {
    https = require('node:https')
} catch (err) {
    console.log(err)
    process.exit()
}
*/

let baseUrl = 'https://lemm.ee'
let headers = {}
let client = new LemmyHttp(baseUrl, headers)
let loginForm = {
  username_or_email: process.env.LEMMY_USER,
  password: process.env.LEMMY_PASS,
}

async function logmein() {
	let jwt = await client.login(loginForm).catch((e) => {console.log(e)})
}

async function getfedobj() {
	let communities = client.getFederatedInstances()
    return communities
}

logmein().catch((e) => {console.log(e)})
let fedobj = getfedobj()
fedobj.then((ret) => {
    let blocked = ret.federated_instances.blocked
    let domains = blocked.map((i) => {
	return i.domain
    })
    let sorto = domains.sort()
    sorto.forEach((i) => {
	let url = 'http://' + i
	https.get(url, resp => {
    		console.log('<div><a href="' + url + '">' + i + '</a></div>')
	})
	.on("error", err => {
	    console.log("<div>ERROR: " + url + " : " + err + "</div>")
	})
    })
})
