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
	let communities = client.listCommunities()
    return communities
}

logmein().catch((e) => {console.log(e)})
let communities = listcom()
communities.then((ret) => {
    /*
    ret.forEach((val) => {
    	console.log(val)
    })
    */
    console.log(ret.communities)
})
//console.log(communities)
