# Initial Public Offering
# A company registers an IPO on a website All the shares on this website are available for a particular time frame called the bidding window, At the end of the bidding an
# auction logic is used to decide how many of the available shares go which bidder until all the shares that are available nave been allotted, or all the bidders have received the shares they bid for.
# comes earlier,
# The bids arrive from the users in the form of < ld, number of shares, bidding price, timestarnp > until the bidding window is closed.
# The auction assigns shares to bidders as follows
# l. The bidder with highest bidding price gets the number of shares they bid for
# 2. If multiple bidders have same bidding prices the bidders are assigned shares the in order in which they bids (earliest bids first)

# Output the list of bidders who don't get any shares i.e. 0 shares in ascending order


def allocateBids(bids, totalShares):
    sorted_bids = sorted(bids, lambda x: [-x[2], x[3]])
    zero_share_bidders = []
    for bid in sorted_bids:
        if totalShares <= 0:
            zero_share_bidders.append(bid[0])
        else:
            totalShares -= bid[1]
    zero_share_bidders.sort()
    return zero_share_bidders
