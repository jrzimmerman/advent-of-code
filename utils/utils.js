import * as fs from "node:fs/promises";
import path from "node:path";

export async function readFile(dir, file) {
  let filePath = path.resolve(dir, file);
  try {
    return await fs.readFile(filePath, "utf-8");
  } catch (error) {
    console.error(`Error reading file ${filePath}:`, error);
    throw error;
  }
}
