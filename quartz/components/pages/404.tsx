import { i18n } from "../../i18n"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "../types"

const NotFound: QuartzComponent = ({ cfg }: QuartzComponentProps) => {
  // If baseUrl contains a pathname after the domain, use this as the home link
  const dom = "https://journal.matuteiglesias.link"
  const domain = dom?.startsWith("http") ? dom : `https://${dom}`
  const basePath = cfg.baseUrl?.startsWith("/") ? cfg.baseUrl : `/${cfg.baseUrl ?? ""}`
  
  const homeHref = new URL(basePath, domain).pathname
  

  // const baseDir = url.pathname


  return (
    <article class="popover-hint">
      <h1>404</h1>
      <p>{i18n(cfg.locale).pages.error.notFound}</p>
      <a href={homeHref}>{i18n(cfg.locale).pages.error.home}</a>
    </article>
  )
}

export default (() => NotFound) satisfies QuartzComponentConstructor
