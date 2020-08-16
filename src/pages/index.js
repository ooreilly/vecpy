import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './styles.module.css';

const features = [

  {
    title: <>GPU accelerated</>,
    imageUrl: 'img/undraw_docusaurus_mountain.svg',
    description: (
      <>
            VecPy is a lightweight GPU accelerated library for performing vectorized operations.
      </>
    ),
  },
  {
    title: <>NumPy-like interface</>,
    imageUrl: 'img/undraw_docusaurus_mountain.svg',
    description: (
      <>
            VecPy lets you perform mathematical operations on vectors with a NumPy-like interface.

      </>
    ),
  },
  {
    title: <>Performance</>,
    imageUrl: 'img/benchmarks/trig_float32.svg',
    description: (
      <>
            VecPy uses just-in-time compilation of pre-optimized compute kernels,  and cacheing to deliver fast performance for both
            small and large array sizes. 
      </>
    ),
  },
];

function Feature({imageUrl, title, description}) {
  const imgUrl = useBaseUrl(imageUrl);
  return (
    <div className={clsx('col col--4', styles.feature)}>
      {imgUrl && (
        <div className="text--center">
          <img className={styles.featureImage} src={imgUrl} alt={title} />
        </div>
      )}
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
}

function Home() {
  const context = useDocusaurusContext();
  const {siteConfig = {}} = context;
  return (
    <Layout
      title={`${siteConfig.title}`}
      description="VecPy: GPU accelerated vector computations">
      <header className={clsx('hero hero--inverse', styles.heroBanner)}>

        <div className="container">
          <h1 className="hero__title">{siteConfig.title}</h1>
          <p className="hero__subtitle">{siteConfig.tagline}</p>

          <img src="img/benchmarks/sum_float32.svg" alt="" />
          <h2>GPU accelerated vector computations in Python. </h2>
          <div className={styles.buttons}>

            <Link
              className={clsx(
                'button button--outline button--secondary button--lg',
                styles.getStarted,
              )}
              to={useBaseUrl('docs/start/vecpy')}>
              Get Started
            </Link>
            <p> &emsp;</p>
            <Link
              className={clsx(
                'button button--outline button--secondary button--lg',
                styles.getStarted,
              )}
              to={'https://github.com/ooreilly/vecpy'}>
              View on Github
            </Link>
          </div>
        </div>
      </header>
      <main>
        {features && features.length > 0 && (
          <section className={styles.features}>
            <div className="container">
            </div>
          </section>
        )}
      </main>
    </Layout>
  );
}

export default Home;
