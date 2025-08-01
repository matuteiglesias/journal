import { truncate } from "node:fs/promises"
import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */

const config: QuartzConfig = {
  configuration: {
    pageTitle: "M.I. Journal",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "en-US",
    // baseUrl: "journal.matuteiglesias.link",
	baseUrl: "/", // or "/subpath" if on a subdomain or subfolder
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "created",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Schibsted Grotesk",
        body: "Source Sans Pro",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#faf8f8",
          lightgray: "#e5e5e5",
          gray: "#b8b8b8",
          darkgray: "#4e4e4e",
          dark: "#2b2b2b",
          secondary: "#284b63",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#fff23688",
        },
        darkMode: {
          light: "#161618",
          lightgray: "#393639",
          gray: "#646464",
          darkgray: "#d4d4d4",
          dark: "#ebebec",
          secondary: "#7b97aa",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#b3aa0288",
        },
      },
    },
  },


  plugins: {
	  transformers: [
	    Plugin.FrontMatter(),
	    Plugin.CreatedModifiedDate({
	      priority: ["frontmatter", "git", "filesystem"],
	    }),
	    Plugin.SyntaxHighlighting({
	      theme: {
		light: "github-light",
		dark: "github-dark",
	      },
	      keepBackground: false,
	    }),
	    
	    Plugin.CrawlLinks({
	      markdownLinkResolution: "absolute",  // safest if your filenames are unique
	      prettyLinks: true,
	      openLinksInNewTab: true,
	      lazyLoad: true,
	      externalLinkIcon: true,
	    }),
	    
	    
	    Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
	    Plugin.GitHubFlavoredMarkdown(),
	    Plugin.TableOfContents(),
	    Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
	    Plugin.Description(),
	    Plugin.Latex({ renderEngine: "katex" }),
	  ],
	  filters: [
	    Plugin.ExplicitPublish(),
	    Plugin.RemoveDrafts(),
	  ],
	  emitters: [
	    Plugin.AliasRedirects(),
	    Plugin.ComponentResources(),
	    Plugin.ContentPage(),
	    Plugin.FolderPage(),
	    Plugin.TagPage(),
	    Plugin.ContentIndex({
	      enableSiteMap: true,
	      enableRSS: true,
	    }),
	    Plugin.Assets(),
	    Plugin.Static(),
	    Plugin.Favicon(),
	    Plugin.NotFoundPage(),
	    // Plugin.CustomOgImages(), // Comment out if you want faster builds

	  ],
	},

	}

export default config
