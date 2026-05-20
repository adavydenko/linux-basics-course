FROM rust:bookworm AS mdbook-builder

ARG MDBOOK_VERSION=0.4.52

RUN cargo install mdbook --version "${MDBOOK_VERSION}"

FROM debian:bookworm-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        fonts-dejavu-core \
        weasyprint \
    && rm -rf /var/lib/apt/lists/*

COPY --from=mdbook-builder /usr/local/cargo/bin/mdbook /usr/local/bin/mdbook
COPY docker/build-mdbook.sh /usr/local/bin/build-mdbook

RUN chmod +x /usr/local/bin/build-mdbook

WORKDIR /workspace

ENTRYPOINT ["build-mdbook"]
CMD ["all"]
