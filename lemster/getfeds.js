#!/usr/bin/env node
import pkg from 'lemmy-js-client';
const { LemmyHttp, Login } = pkg;
//import { LemmyHttp, Login } from 'lemmy-js-client'

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

async function listcom() {
	let communities = client.getFederatedInstances()
    return communities
}

logmein().catch((e) => {console.log(e)})
let communities = listcom()
communities.then((ret) => {
    let blocked = ret.federated_instances.blocked
    let domains = blocked.map((i) => {
	return i.domain
    })
    domains.sort().forEach((i) => {
    	console.log(i)
    })
})
