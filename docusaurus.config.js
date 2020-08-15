const math = require('remark-math')
const remark2rehype = require('remark-rehype')
const katex = require('rehype-katex')

module.exports = {
  title: 'VecPy',
  tagline: '',
  url: 'https://ooreilly.github.io/',
  baseUrl: '/vecpy/',
  onBrokenLinks: 'throw',
  favicon: 'img/favicon.ico',
  organizationName: 'ooreilly', // Usually your GitHub org/user name.
  projectName: 'vecpy', // Usually your repo name.
 stylesheets: [
    // String format.
    'https://cdn.jsdelivr.net/npm/katex@0.11.0/dist/katex.min.css', 
    // Object format.
    {
      //href: 'http://mydomain.com/style.css',
      href: 'https://cdn.jsdelivr.net/npm/katex@0.11.0/dist/katex.min.css', 
      type: 'text/css',
    },
 ],
  themeConfig: {
    navbar: {
      title: 'VecPy',
      logo: {
        alt: 'My Site Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          to: 'docs/start/vecpy',
          activeBasePath: 'docs',
          label: 'Docs',
          position: 'left',
        },
        {
          to: 'docs/benchmarks/sum',
          activeBasePath: 'benchmarks',
          label: 'Performance',
          position: 'left',
        },
        //{to: 'blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/ooreilly/vecpy',
          label: 'GitHub',
          position: 'left',
        },
      ],
    },
    footer: {
      style: 'dark',
      //links: [
      //  {
      //    title: 'Docs',
      //    items: [
      //      {
      //        label: 'Style Guide',
      //        to: 'docs/',
      //      },
      //      {
      //        label: 'Second Doc',
      //        to: 'docs/doc2/',
      //      },
      //    ],
      //  },
      //  //{
      //  //  title: 'More',
      //  //  items: [
      //  //    {
      //  //      label: 'Blog',
      //  //      to: 'blog',
      //  //    },
      //  //    {
      //  //      label: 'GitHub',
      //  //      href: 'https://github.com/ooreilly/vecpy',
      //  //    },
      //  //  ],
      //  //},
      //],
      copyright: `Copyright © ${new Date().getFullYear()} VecPy. Built with Docusaurus.`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          // It is recommended to set document id as docs home page (`docs/` path).
          homePageId: 'index',
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl:
            'https://github.com/ooreilly/vecpy',
          remarkPlugins: [
                    math,
          ],
          rehypePlugins: [[katex, {strict: false}]],
        },
        //blog: {
        //  showReadingTime: true,
        //  // Please change this to your repo.
        //  editUrl:
        //    'https://github.com/ooreilly/vecpy',
        //},
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
