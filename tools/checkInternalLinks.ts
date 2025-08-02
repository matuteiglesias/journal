import fs from "fs";
import path from "path";

// === Configuration ===
const contentDir = path.join(process.cwd(), "content");

function extractLinks(markdown: string): string[] {
  const wikiLinks = [...markdown.matchAll(/\[\[([^\]]+)\]\]/g)].map(m => m[1]);
  const mdLinks = [...markdown.matchAll(/\[.*?\]\((.*?)\)/g)].map(m => m[1]);
  return [...wikiLinks, ...mdLinks].filter(link => !link.startsWith("http"));
}

function slugify(filename: string): string {
  return filename.toLowerCase().replace(/\s+/g, "-").replace(/\.md$/, "").replace(/\//g, "");
}

const allFiles = fs.readdirSync(contentDir, { withFileTypes: true });
const validMarkdownFiles = allFiles
  .filter(entry => entry.isFile() && entry.name.endsWith(".md"))
  .map(entry => entry.name);

const slugs = new Set(validMarkdownFiles.map(f => slugify(f)));

for (const file of validMarkdownFiles) {
  const fullPath = path.join(contentDir, file);
  const text = fs.readFileSync(fullPath, "utf-8");
  const links = extractLinks(text);
  for (const link of links) {
    const slug = slugify(link);
    if (!slugs.has(slug)) {
      console.warn(`❌ Broken link in ${file}: [[${link}]] → slugified: ${slug}`);
    }
  }
}
