/**
 * Download input and save to input.txt
 */

import * as fs from "node:fs/promises";
import path from "path";

const SESSION_TOKEN = process.env.SESSION_TOKEN;
const EMAIL = process.env.EMAIL;
const baseUrl = "https://adventofcode.com";
const year = process.argv[2] || "2025";
console.log("year: " + year);
const day = process.argv[3] || "1";
console.log("day: " + day);
const url = `${baseUrl}/${year}/day/${day}/input`;
console.log("url: " + url);

async function getInput() {
  try {
    const resp = await fetch(url, {
      headers: {
        Cookie: `session=${SESSION_TOKEN}`,
        "User-Agent": `${EMAIL}`,
      },
    });
    if (!resp.ok) {
      throw new Error(`HTTP error! Status: ${resp.status}`);
    }
    const text = await resp.text();
    return text;
  } catch (error) {
    console.error(error);
    throw error;
  }
}

async function saveInput(year, day, input) {
  const padDay = day.padStart(2, "0");
  const dir = `./${year}/day${padDay}`;
  try {
    await fs.mkdir(dir, { recursive: true });
    const filePath = path.join(dir, "input.txt");
    await fs.writeFile(filePath, input);
    console.log(`saved to ${filePath}`);
  } catch (error) {
    console.error(error);
  }
}

const input = await getInput();
saveInput(year, day, input);
