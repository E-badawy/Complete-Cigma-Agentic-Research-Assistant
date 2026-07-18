function PaperCard({ paper }) {
    return (
        <div className="border rounded-xl p-5 hover:shadow-md transition">

            <h3 className="text-lg font-semibold text-slate-800">
                {paper.title || "Untitled"}
            </h3>

            <div className="mt-2 text-sm text-gray-600">

                <p>

                    <strong>Authors:</strong>{" "}

                    {paper.authors?.length
                        ? paper.authors.join(", ")
                        : "Unknown"}

                </p>

                <p>

                    <strong>Journal:</strong>{" "}

                    {paper.journal || "Unknown"}

                </p>

                <p>

                    <strong>Year:</strong>{" "}

                    {paper.year || "Unknown"}

                </p>

                <p>

                    <strong>Citations:</strong>{" "}

                    {paper.citations ?? "N/A"}

                </p>

            </div>

            {paper.abstract && (

                <details className="mt-4">

                    <summary className="cursor-pointer font-medium text-blue-600">
                        View Abstract
                    </summary>

                    <p className="mt-3 text-gray-700 leading-7">
                        {paper.abstract}
                    </p>

                </details>

            )}

            {paper.doi && (

                <a
                    href={`https://doi.org/${paper.doi}`}
                    target="_blank"
                    rel="noreferrer"
                    className="inline-block mt-5 text-blue-600 hover:underline"
                >
                    View DOI →
                </a>

            )}

        </div>
    );
}

export default PaperCard;