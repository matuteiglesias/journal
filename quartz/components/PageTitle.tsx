import { pathToRoot } from "../util/path"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"
import { i18n } from "../i18n"

const PageTitle: QuartzComponent = ({ fileData, cfg, displayClass }: QuartzComponentProps) => {
  const title = cfg?.pageTitle ?? i18n(cfg.locale).propertyDefaults.title
  const baseDir = pathToRoot(fileData.slug!)
  return (
    <h1 class={classNames(displayClass, "page-title")}>
      <div class="title-logo">
        <a href={baseDir}>
          <img id="icon-header" src="/static/my-icon.png" alt="Home" />
        </a>
        <a href={baseDir} class="header-text">
          {title}
        </a>
      </div>
    </h1>
  )
}

PageTitle.css = `
.page-title {
  font-size: 1.75rem;
  margin: 0;
  text-align: center;
}

.title-logo {
  display: flex;
  flex-direction: column;  /* stack vertically */
  align-items: center;     /* center horizontally */
  gap: 0.5rem;
  margin-top: 1rem;
  margin-bottom: 1rem;
}

#icon-header {
  max-height: 120px;
}

.header-text {
  font-family: var(--titleFont);
  font-weight: bold;
  font-size: 1.8rem;
  text-decoration: none;
  color: inherit;
}
`

export default (() => PageTitle) satisfies QuartzComponentConstructor